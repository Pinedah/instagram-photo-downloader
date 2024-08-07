#! python3
# main.py - simple script that downloads every single photo in an Instagram profile given

import requests, os, bs4, logging

logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s -  %(levelname)s -   %(message)s')
# logging.disable(logging.CRITICAL)

instagra_url = "https://www.instagram.com/"
instagram_profile = ''

os.makedirs('photos', exist_ok=True)

instagram_profile = input("\nEnter the Instagram Profile: ")

"""
for i in range(5):
    # Download the page
    print(f"Downloading the page... {url}")
    res = requests.get(url)
    res.raise_for_status()

    logging.info(res.text)
    soup = bs4.BeautifulSoup(res.text, features='html.parser')

    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')

    logging.info(comicElem)
    logging.info(len(comicElem))
    logging.info(comicElem[0].attrs)
    logging.info(comicElem[0].get('src'))

    if comicElem == []:
        print("Could not find comic image.")
    else:
        comicUrl = 'https://xkcd.com' + comicElem[0].get('src')
        # Download the image
        print(f"\nDownloading the image... {comicUrl}")
        
        res = requests.get(comicUrl)
        res.raise_for_status()

        # Save the image to ./xkcd
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb') # opened in write binarymode
    
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
        

    # Get the Prev button's url
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print("\nDONE.")
"""