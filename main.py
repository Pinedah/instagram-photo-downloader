#! python3
# main-login.py - Simple script that download all photos from an Instagram profile (LogIn manually).

# Import libraries and modules 
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


def main():
    print("\n--- Please checkout the README file before using the script :). ---\n")
    print("Login into your account and then go to the profile you want to scrapp.")
    print("When you are ready, press ENTER in the console to begin the downloads.\n\n")

    # Initialize browser object
    browser = webdriver.Chrome()
    browser.get('https://www.instagram.com/')
    time.sleep(2)

    input()


    try:
        htmlElem = browser.find_element(By.TAG_NAME, 'html')
        logging.critical("encuentra elemento html")
        time.sleep(4)


        logging.critical("account name")
        accountName = get_profile_name(browser)
        logging.critical("END account name")
        posts = get_number_of_posts(browser)
        logging.critical("END number of posts")
        time.sleep(2)


        logging.critical("intenta scrollable")

        scrollable_div = browser.find_element(By.CSS_SELECTOR, "._9dls._ar44.js-focus-visible._aa4d")

        logging.critical(scrollable_div)
        logging.critical("END  scrollable")
        
        #usersList = []
        Flag = True
        while Flag:
            # Look if we are in the final of the div
            logging.critical("EXECUTE SCRITP")
            at_bottom = browser.execute_script(
                "return arguments[0].scrollTop + arguments[0].clientHeight >= arguments[0].scrollHeight;", 
                scrollable_div)
            
            at_bottom = browser.execute_script("""
                return arguments[0].scrollTop + arguments[0].clientHeight >= arguments[0].scrollHeight;
                """, scrollable_div)
            
            if at_bottom:
                logging.info("End page.")
                Flag = False  
            
            else:
                logging.critical("intenta div elem")
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



if __name__ == '__main__':
    main()