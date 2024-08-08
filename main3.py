import logging
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Starting...")

# Set up Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  # Run in headless mode

# Path to your ChromeDriver executable
chrome_driver_path = "C:\\Users\\Dell Latitude\\Documents\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"

logging.info("Chrome path given...")

# Set up the Chrome driver
services = Service(chrome_driver_path)
driver = webdriver.Chrome(service=services, options=chrome_options)
logging.info("Driver object created...")

# Open the Instagram profile page
profile_url = "https://www.instagram.com/pinedah_11/"
driver.get(profile_url)

# Allow time for the page to load
time.sleep(5)  # Increase sleep time to ensure the page loads completely

# Scroll to load more images (optional)
scroll_pause_time = 2
for _ in range(5):  # Adjust the range to load more/less images
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(scroll_pause_time)

# Find image elements
image_elements = driver.find_elements(By.TAG_NAME, 'img')
logging.info(f"Found {len(image_elements)} image elements.")

# Download images
for index, image_element in enumerate(image_elements):
    image_url = image_element.get_attribute('src')
    if image_url:  # Check if the image URL exists
        print(f"Downloading image {index + 1}: {image_url}")
        img_data = requests.get(image_url).content
        with open(f'image_{index + 1}.jpg', 'wb') as handler:
            handler.write(img_data)
    else:
        logging.warning(f"Image URL not found for element {index + 1}")

# Close the browser
driver.quit()  # Correctly close the browser
