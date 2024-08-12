#! python3
# scrapping photos an instagram profile

import logging, time, webbrowser, requests, os
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s -  %(levelname)s -   %(message)s')
#logging.disable(logging.CRITICAL)

## CLEAN THE CODE!

def download_photos(imagesLinks, imageNames):
    os.makedirs('photos-samuel', exist_ok=True)
    #os.chdir("photos-samuel")
    for i in range(len(imagesLinks)):
        response = requests.get(imagesLinks[i])
        # Ensure the request was successful
        if response.status_code == 200:
            # Save the image to a file
            logging.info(str(imageNames[i]))
            nameDebugged = str(imagesLinks[i]).replace("/", "").replace(".", "").replace(":","").replace("\n", "").replace("\\", "").replace("#", "").replace(":", "").replace("*", "").replace("?", "").replace("\"", "").replace("<", "").replace(">", "")[:100] + '-' + str(imageNames[i]).replace("\n", "").replace("\\", "").replace("#", "").replace(":", "").replace("*", "").replace("?", "").replace("\"", "").replace("<", "").replace(">", "")[:100]
            logging.info(nameDebugged)
            #with open(f"\photos-mewton\{str(imageNames[i]).replace("\\n", "")}.jpg", "wb") as file:
            with open(f"photos-samuel\\{nameDebugged}.jpg", "wb") as file:
                file.write(response.content)
            print("Image downloaded successfully!")
        else:
            print(f"Failed to download image. Status code: {response.status_code}")


users = ['pinedah_11', 'faatii._01', 'samueln.ortigoza', 'mewton_the_cat']
# users = {'tags': ['pinedah_11', 'faatii._01', 'samueln.ortigoza', 'mewton_the_cat'], 'posts': [7, 4, 465, 30]}

browser = webdriver.Chrome()
browser.get('https://www.instagram.com/' + users[2])

time.sleep(5)

try:

    loginButton = browser.find_element(By.LINK_TEXT, 'Log In')
    loginButton.click()

    time.sleep(4)

    emailForm = browser.find_elements(By.TAG_NAME, 'input')
    emailForm[0].click()
    emailForm[0].send_keys('papanacho11')
    time.sleep(2)
    # emailForm.send_keys(Keys.TAB)
    time.sleep(2)
    emailForm[1].click()
    emailForm[1].send_keys('Papanachito')
    time.sleep(2)
    emailForm[1].submit()

    #emailForm.send_keys(Keys.ENTER)

    
    time.sleep(4)
    notnow = browser.find_element(By.TAG_NAME, 'button')
    notnow.click()

    time.sleep(2)

    htmlElem = browser.find_element(By.TAG_NAME, 'html')

    numberOfPosts = browser.find_element(By.CLASS_NAME, 'xdj266r') # find the number of posts

    
    # TODO: Add the math expression neccessary to in function to the number of posts, define the scrolls
    for _ in range(50): 

        div_elem = browser.find_elements(By.CLASS_NAME, '_aagv')

        img_elems = []
        srcs = []
        alts = []
        for i in range(len(div_elem)):
            img_elems.append(div_elem[i].find_element(By.TAG_NAME, 'img'))

        for j in range(len(img_elems)):
            srcs.append(img_elems[j].get_attribute('src'))
            alts.append(img_elems[j].get_attribute('alt'))

        download_photos(srcs, alts)
        htmlElem.send_keys(Keys.END)
        time.sleep(2)

    # DOWNLOAD THE PHOTOS

    logging.info(len(srcs))
    logging.info(srcs)

    # Send a GET request to the image URL
    """os.makedirs('photos-samuel', exist_ok=True)
    for i in range(len(srcs)):

        response = requests.get(srcs[i])
        # Ensure the request was successful
        if response.status_code == 200:
            # Save the image to a file
            with open(f"photos-samuel\photo{i+1}.jpg", "wb") as file:
                file.write(response.content)
            print("Image downloaded successfully!")
        else:
            print(f"Failed to download image. Status code: {response.status_code}")"""


except NoSuchElementException:
    print("Was not able to find an element with that class name.")

# Wait for user input before closing the browser
input("Press Enter to close the browser...")
logging.info(numberOfPosts.text)

# Close the browser
browser.quit()
