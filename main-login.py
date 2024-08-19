#! python3
# main-login.py - Simple script that download all photos from an Instagram profile (LogIn manually).

import logging, time, requests, os, re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s -  %(levelname)s -   %(message)s')
logging.disable(logging.DEBUG)

def clean_file_names(folderPath):
    os.chdir(folderPath)
    i = 0
    for file in os.listdir(os.curdir):
        os.rename(file, 'Photo ' + str(i) + ' - ' + str(file).split('---cut---')[1])
        i += 1

def get_profile_name(profile):
    profileInfo = profile.find_element(By.CLASS_NAME, 'xdj266r') # find the number of posts
    infoByLines = str(profileInfo.text).split('\n')
    tag = infoByLines[0]
    return tag

def get_number_of_posts(profile):
    profileInfo = profile.find_element(By.CLASS_NAME, 'xdj266r') # find the number of posts
    infoByLines = str(profileInfo.text).split('\n')
    posts = infoByLines[3].split(' ')
    return int(posts[0])

def download_photos(imagesLinks, imageNames, user):
    
    os.makedirs(f'photos-{user}', exist_ok = True)
    pattern = r"[\/.:\\#*?\"<>]"
    
    for i in range(len(imagesLinks)):
        response = requests.get(imagesLinks[i])
        # Ensure the request was successful
        if response.status_code == 200:
            # Save the image to a file
            nameDebugged = re.sub(pattern, "", str(imagesLinks[i])).replace("\n", "")[:100] + '---cut---'+ re.sub(pattern, "", str(imageNames[i])).replace("\n", "")[:100]

            with open(f"photos-{user}\\{nameDebugged}.jpg", "wb") as file:
                file.write(response.content)
            print(f"Image downloaded successfully!")
        else:
            print(f"Failed to download image. Status code: {response.status_code}")


# -------------------- BEGIN CODE -----------------------------------------------
# TODO: Add Main !!

print("\n--- Please checkout the README file before using the script :). ---\n")
print("Login into your account and then go to the profile you want to scrapp.")

browser = webdriver.Chrome()
browser.get('https://www.instagram.com/')

input("When you are ready, press ENTER in the console")
time.sleep(2)

try:
    htmlElem = browser.find_element(By.TAG_NAME, 'html')
    time.sleep(4)

    accountName = get_number_of_posts(browser)
    posts = get_number_of_posts(browser)
    time.sleep(2)

    for _ in range(round(posts / 34)):
        
        div_elem = browser.find_elements(By.CLASS_NAME, '_aagv')
        img_elems = []
        srcs = []
        alts = []

        for i in range(len(div_elem)):
            img_elems.append(div_elem[i].find_element(By.TAG_NAME, 'img'))

        for j in range(len(img_elems)):
            srcs.append(img_elems[j].get_attribute('src'))
            alts.append(img_elems[j].get_attribute('alt'))

        download_photos(srcs, alts, accountName)

        for _ in range(3):
            htmlElem.send_keys(Keys.END)
            time.sleep(2)
            
except NoSuchElementException:
    print("Was not able to find an element with that class name.")


clean_file_names(f'photos-' + accountName)

browser.quit()

print("\n\nThanks for scrapping with us, come again soon!!<3<3 \n\n")