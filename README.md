# Instagram Photo Downloader

This project is a Python-based scraper that allows you to download all photos from a public Instagram profile or a Profile you have access to. The script automates the process of retrieving images, making it easy to back up or analyze content from any accessible Instagram account.

## Features

- **Download All Photos:** Automatically download all photos from a specified public Instagram profile.
- **Easy Setup:** Simple installation and configuration process.
- **Error Handling:** Built-in error handling to manage issues like rate limits or connectivity problems.

## Requirements

Before running the scraper, ensure you have the following installed:

- Python 3.x
- Requests library (pip install requests)
- BeautifulSoup library (pip install beautifulsoup4)
- Selenium library (pip install selenium)
- Pprint (PrettyPrint) library (pip install pprintpp) (Optional, as pprint is included in the Python standard library. Install only if extended functionality is needed.)
- Logging library (Already included in the Python standard library, no installation needed.)
- OS library (Already included in the Python standard library, no installation needed.)
- RE (Regular Expressions) library (Already included in the Python standard library, no installation needed.)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Pinedah/instagram-photo-downloader.git

2. **Install the required Python libraries:**
   Requirements given before.
   
3. **Run the script you prefer:**
   ```bash
   main.py or main-login.py

## Usage -> MAIN AND MAIN-LOGIN

1. Main <br>
With main.py, you can download photos fully automatically (no login necessary) from any public Instagram account.

2. Main-Login <br>
With main-login.py, you will need to log in to your Instagram account. Once Instagram has loaded, log in manually, then press enter in the console, and the downloads will begin. This script allows you to scrape photos from a private account that you follow.

## DISCLAIMER 
Script built with the only purpose to practice web scraping in python. Be aware.

Peace.
