#! python3
# scrapping photos an instagram profile

# still need to add ability to know when all photos are scraped and quit the browser

import tkinter as tk
from tkinter import messagebox, scrolledtext
import time, requests, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, WebDriverException, NoSuchWindowException
import re

def clean_file_names(image_name):
    # Replacing invalid characters with an underscore or remove them
    cleaned_name = re.sub(r'[\/:*?"<>|\n]', "", image_name)
    return cleaned_name

def download_photos(imagesLinks, imageNames):
    os.makedirs('Photos', exist_ok=True)
    for i in range(len(imagesLinks)):
        try:
            response = requests.get(imagesLinks[i], timeout=10)  # Set a timeout for the request
            if response.status_code == 200:
                cleaned_image_name = clean_file_names(imageNames[i])[:100]
                file_name = f"Photos\\{cleaned_image_name}.jpg"
                with open(file_name, "wb") as file:
                    file.write(response.content)
                status_label.config(text=f"Image '{cleaned_image_name}' downloaded successfully!")
                log_text.insert(tk.END, f"Downloaded: {cleaned_image_name}\n")
            else:
                status_label.config(text=f"Failed to download image. Status code: {response.status_code}")
                log_text.insert(tk.END, f"Failed to download image. Status code: {response.status_code}\n")
        except requests.exceptions.RequestException as e:
            status_label.config(text=f"Network error occurred: {e}")
            log_text.insert(tk.END, f"Network error occurred: {e}\n")
            break
        except OSError as e:
            status_label.config(text=f"File saving error: {e}")
            log_text.insert(tk.END, f"File saving error: {e}\n")
            continue

def scrape_photos():
    username = username_entry.get()
    if not username:
        messagebox.showwarning("Input Error", "Please enter an Instagram username.")
        return
    
    browser = None
    try:
        status_label.config(text="Opening browser and navigating to Instagram...")
        log_text.insert(tk.END, "Opening browser and navigating to Instagram...\n")
        browser = webdriver.Chrome()
        browser.get(f'https://www.instagram.com/{username}/')

        time.sleep(5)

        try:
            private_message = browser.find_elements(By.XPATH, "//*[contains(text(), 'This Account is Private')]")
            if private_message:
                status_label.config(text="The account is private and not scrapeable.")
                log_text.insert(tk.END, "The account is private and not scrapeable.\n")
            else:
                status_label.config(text="Account is public. Scraping images...")
                log_text.insert(tk.END, "Account is public. Scraping images...\n")

                # Waiting for the "Show more posts" button to be clickable
                try:
                    show_more_button = WebDriverWait(browser, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Show more posts')]"))
                    )
                    browser.execute_script("arguments[0].scrollIntoView();", show_more_button)
                    show_more_button.click()
                    time.sleep(3)
                except NoSuchElementException:
                    pass
                except Exception as e:
                    log_text.insert(tk.END, f"Error clicking 'Show more posts' button: {e}\n")
                    status_label.config(text=f"Error clicking 'Show more posts' button: {e}")
                    return

                while True:
                    div_elem = browser.find_elements(By.CLASS_NAME, '_aagv')
                    if not div_elem:
                        break
                    
                    img_elems = [div.find_element(By.TAG_NAME, 'img') for div in div_elem]

                    srcs = [img.get_attribute('src') for img in img_elems]
                    alts = [img.get_attribute('alt') for img in img_elems]

                    download_photos(srcs, alts)
                    browser.find_element(By.TAG_NAME, 'html').send_keys(Keys.END)
                    time.sleep(2)

                    # Checking if all images have been loaded
                    if len(srcs) == 0:
                        break

                status_label.config(text="Scraping completed!")
                log_text.insert(tk.END, "Scraping completed!\n")

        except NoSuchElementException:
            status_label.config(text="Error: Unable to find the required element.")
            log_text.insert(tk.END, "Error: Unable to find the required element.\n")
        
        except NoSuchWindowException:
            status_label.config(text="Error: Browser window was closed unexpectedly.")
            log_text.insert(tk.END, "Error: Browser window was closed unexpectedly.\n")

    except WebDriverException as e:
        status_label.config(text=f"WebDriver error: {str(e)}")
        log_text.insert(tk.END, f"WebDriver error: {str(e)}\n")
    
    finally:
        if browser:
            try:
                browser.quit()
                status_label.config(text="Browser closed.")
                log_text.insert(tk.END, "Browser closed.\n")
            except WebDriverException as e:
                status_label.config(text=f"Error closing the browser: {e}")
                log_text.insert(tk.END, f"Error closing the browser: {e}\n")

# Tkinter GUI setup with dark theme
root = tk.Tk()
root.title("Instagram Photo Scraper")
root.geometry("600x425")
root.configure(bg='#2b2b2b')

# Username Label and Entry
username_frame = tk.Frame(root, bg='#2b2b2b')
username_frame.pack(pady=20, padx=20, fill='x')

username_label = tk.Label(username_frame, text="Instagram Username:", bg='#2b2b2b', fg='white', font=("Helvetica", 14))
username_label.pack(side='left')

username_entry = tk.Entry(username_frame, width=40, bg='#3c3f41', fg='white', insertbackground='white', font=("Helvetica", 14))
username_entry.pack(side='left', padx=10)

# Scrape Button
scrape_button = tk.Button(root, text="Scrape Photos", command=scrape_photos, bg="#5a5a5a", fg="white", font=("Helvetica", 14), width=20)
scrape_button.pack(pady=10)

# Status Label
status_label = tk.Label(root, text="", bg='#2b2b2b', fg='white', font=("Helvetica", 12))
status_label.pack(pady=10)

# Log Section
log_text = scrolledtext.ScrolledText(root, bg='#3c3f41', fg='white', font=("Helvetica", 12), height=10, wrap=tk.WORD)
log_text.pack(pady=10, padx=10, fill='both')

# Start the GUI loop
root.mainloop()
