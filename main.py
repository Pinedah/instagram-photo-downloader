#! python3
# main.py - Simple script that download all photos from a public Instagram profile.

import logging, time, requests, os, re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s -  %(levelname)s -   %(message)s')
logging.disable(logging.CRITICAL)

def clean_file_names(folderPath):
    os.chdir(folderPath)
    i = 0
    for file in os.listdir(os.curdir):
        os.rename(file, 'Photo ' + str(i) + ' - ' + str(file).split('---cut---')[1])
        i += 1

def get_number_of_posts(profile):
    profileInfo = profile.find_element(By.CLASS_NAME, 'xdj266r') # find the number of posts
    infoByLines = str(profileInfo.text).split('\n')
    posts = infoByLines[3].split(' ')
    return int(posts[0])

def download_photos(imagesLinks, imageNames, user):
    
    os.makedirs(f'photos-{user}', exist_ok=True)
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
# TODO: Add Main and UI !!

# THIS ACCOUNT WAS CREATED JUST TO TEST, PLEASE DO NOT CHANGE THE CREDENTIALS
scrapperUser = "papanacho11"
scrapperPassword = "Papanachito"

accountName = str(input("\n\nEnter the account name to scrapp (check the README).\n"))

browser = webdriver.Chrome()
browser.get('https://www.instagram.com/' + accountName)

time.sleep(4)

try:

    loginButton = browser.find_element(By.LINK_TEXT, 'Log In')
    loginButton.click()

    time.sleep(2)

    emailForm = browser.find_elements(By.TAG_NAME, 'input')
    emailForm[0].click()
    emailForm[0].send_keys(scrapperUser)
    time.sleep(2)
    emailForm[1].click()
    emailForm[1].send_keys(scrapperPassword)
    time.sleep(1.5)
    emailForm[1].submit()
    time.sleep(5.2)
    notnow = browser.find_element(By.TAG_NAME, 'button')
    notnow.click()

    time.sleep(5)

    htmlElem = browser.find_element(By.TAG_NAME, 'html')

    time.sleep(4)
    posts = get_number_of_posts(browser)
    logging.info(posts)
    time.sleep(2)

    for _ in range(max(round(posts / 25), 2)):

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

print(f"\n\n{len(os.listdir(os.curdir))} photos downloaded...")
print("Thanks for scrapping with us, come again soon!!<3<3 \n\n")

browser.quit()