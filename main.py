#! python3
# scrapping photos an instagram profile

import logging, time, webbrowser, requests, os, pprint
import re

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

def get_number_of_posts(profile):
    numberOfPosts = profile.find_element(By.CLASS_NAME, 'xdj266r') # find the number of posts
    logging.info(numberOfPosts.text)
    posts = str(numberOfPosts.text).split('\n')
    logging.info(posts)
    p = posts[3].split(' ')
    logging.info(p)
    return int(p[0])

def download_photos(imagesLinks, imageNames, user):
    
    os.makedirs(f'photos-{users[choice]}', exist_ok=True)
    pattern = r"[\/.:\\#*?\"<>]"
    
    for i in range(len(imagesLinks)):
        response = requests.get(imagesLinks[i])
        # Ensure the request was successful
        if response.status_code == 200:
            # Save the image to a file

            logging.info(str(imageNames[i]))
            nameDebugged = re.sub(pattern, "", str(imagesLinks[i])).replace("\n", "")[:100] + '---cut---'+ re.sub(pattern, "", str(imageNames[i])).replace("\n", "")[:100]
            
            logging.info(nameDebugged)
            with open(f"photos-{user}\\{nameDebugged}.jpg", "wb") as file:
                file.write(response.content)
            print("Image downloaded successfully!")
        else:
            print(f"Failed to download image. Status code: {response.status_code}")


users = ['pinedah_11', 'faatii._01', 'samueln.ortigoza', 'mewton_the_cat']

# TODO: Make the user enters the account name
print(f"Select the user (0,1,2,3): \n{users}")
choice = int(input())

browser = webdriver.Chrome()
browser.get('https://www.instagram.com/' + users[choice])

time.sleep(5)

try:

    loginButton = browser.find_element(By.LINK_TEXT, 'Log In')
    loginButton.click()

    time.sleep(4)

    emailForm = browser.find_elements(By.TAG_NAME, 'input')
    emailForm[0].click()
    emailForm[0].send_keys('papanacho11')
    time.sleep(2)
    time.sleep(2)
    emailForm[1].click()
    emailForm[1].send_keys('Papanachito')
    time.sleep(2)
    emailForm[1].submit()
    time.sleep(4)
    notnow = browser.find_element(By.TAG_NAME, 'button')
    notnow.click()

    time.sleep(2)

    htmlElem = browser.find_element(By.TAG_NAME, 'html')

    time.sleep(2)
    posts = get_number_of_posts(browser)
    logging.info(posts)
    time.sleep(1)

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

        download_photos(srcs, alts, users[choice])
        htmlElem.send_keys(Keys.END)
        time.sleep(2)
        htmlElem.send_keys(Keys.END)
        time.sleep(2)
        htmlElem.send_keys(Keys.END)
        time.sleep(2)


    logging.info(len(srcs))
    logging.info(srcs)

except NoSuchElementException:
    print("Was not able to find an element with that class name.")


clean_file_names(f'photos-' + users[choice])

browser.quit()

os.chdir('photos-' + users[choice])
print(str(len(os.listdir(os.curdir))) + ' photos downloaded!')