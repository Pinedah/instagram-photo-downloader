#! python3
# main.py - Simple script that download all photos from an Instagram profile (LogIn manually).

# General libraries and modules 
import logging, time, requests, os, re

# Library to scrapp
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

# View libraries
import tkinter as tk

# Debugging Tools
logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s -  %(levelname)s -   %(message)s')
logging.disable(logging.CRITICAL) # .CRITICAL to disable all logging messages

def clean_file_names(folderPath):
    os.chdir(folderPath) # change to the downloaded photos dir
    i = 1
    for file in os.listdir(os.curdir):
        os.rename(file, f"Photo {str(i)} - {str(file).split('---cut---')[1]}") # rename each photo
        i += 1

def get_profile_name(profile):
    profileInfo = profile.find_element(By.CLASS_NAME, 'xdj266r') 
    infoByLines = str(profileInfo.text).split('\n')
    tag = infoByLines[0]
    return tag

def download_photos(imagesLinks, imageNames, user):
    
    os.makedirs(f'photos-{user}', exist_ok = True) # create the directory where photos will be stored
    pattern = r"[\/.:\\#*?\"<>]" # define a regex expression 
    
    for i in range(len(imagesLinks)):
        response = requests.get(imagesLinks[i])
        
        # Ensure the request was successful
        if response.status_code == 200: # Save the image to a file

            # debug the img name 
            nameDebugged = re.sub(pattern, "", str(imagesLinks[i])).replace("\n", "")[:100] + '---cut---' + re.sub(pattern, "", str(imageNames[i])).replace("\n", "").replace("|", "")[:100]

            with open(f"photos-{user}\\{nameDebugged}.jpg", "wb") as file: # save image in the folder
                file.write(response.content)
        else:
            print(f"Failed to download image. Status code: {response.status_code}")

def scrap(browser, view):
    try:
        htmlElem = browser.find_element(By.TAG_NAME, 'html') # get general html object
        time.sleep(2) # let webpage to load

        accountName = get_profile_name(browser)
        # posts = get_number_of_posts(browser)
        time.sleep(1) # let webpage to load

        scrollable_div = browser.find_element(By.CSS_SELECTOR, "._9dls._ar44.js-focus-visible._aa4d")
        
        Flag = True
        while Flag:

            # Look if we are in the final of the div
            at_bottom = browser.execute_script("""
                return arguments[0].scrollTop + arguments[0].clientHeight >= arguments[0].scrollHeight;
                """, scrollable_div)
            
            if at_bottom:
                Flag = False  
            else:
                div_elem = browser.find_elements(By.CLASS_NAME, '_aagv')
                img_elems = [] 
                srcs = [] # get the url of each img
                alts = [] # get the alt (may be the description in a post, if there is no desc, it'll be the date)

                for i in range(len(div_elem)):
                    img_elems.append(div_elem[i].find_element(By.TAG_NAME, 'img'))

                for j in range(len(img_elems)): # get src's and alt's from the img objects
                    srcs.append(img_elems[j].get_attribute('src'))
                    alts.append(img_elems[j].get_attribute('alt'))

                download_photos(srcs, alts, accountName)

                for _ in range(3): # scroll down the page
                    htmlElem.send_keys(Keys.END)
                    time.sleep(2)

        clean_file_names(f'photos-' + accountName)

        # print the number of photos in a label at the end
        label_title4 = tk.Label(view, text=f"{len(os.listdir(os.curdir))} photos downloaded... \nThanks for scrapping with us, come again soon!!<3<3 ", font=("Arial", 10), fg="white", bg="black")
        label_title4.pack(padx=10, pady=10)
        os.chdir("..")

    except NoSuchElementException:
        print("Was not able to find an element with that class name.")


def view(browser):

    # configure main view
    view = tk.Tk()
    view.title("INSTAGRAM PHOTO-SCRAPPER")
    view.geometry("500x300")  
    view.configure(bg="black")  
    view.resizable(False, False)

    # set view icon
    icono = tk.PhotoImage(file="pank.png")  
    view.iconphoto(False, icono)

    # label for the title
    label_title = tk.Label(view, text="INSTAGRAM PHOTO-SCRAPPER", font=("Arial", 20), fg="white", bg="black")
    label_title.pack(padx=10, pady=5)

    # label for the readme suggest
    readme_info = f"Please checkout the README file before using the script :)"
    label_title2 = tk.Label(view, text=readme_info, font=("Arial", 9), fg="white", bg="black")
    label_title2.pack(padx=10, pady=3)

    # label for general info
    info = r"""
    Login into your account and then go to the profile you want to scrapp
    When you are ready, press the DOWNLOAD button to begin"""
    label_title3 = tk.Label(view, text=info, font=("Arial", 11), fg="white", bg="black")
    label_title3.pack(padx=10, pady=1)
    
    # button to start scrapping
    btn_start_scrapping = tk.Button(view, text="DOWNLOAD", command = lambda: scrap(browser, view), fg="white", bg="black", border=2)
    btn_start_scrapping.pack(padx= 10, pady=5)

    # main view loop
    view.mainloop()


def main():

    # Initialize browser object
    browser = webdriver.Chrome()
    browser.get('https://www.instagram.com/')
    
    # call UI
    view(browser)

    browser.quit() # close the web browser

if __name__ == '__main__':
    main()