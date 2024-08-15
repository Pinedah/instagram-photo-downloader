import logging, time, requests, os, pprint, re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s -  %(levelname)s -   %(message)s')
logging.disable(logging.DEBUG)

browser = webdriver.Chrome()
browser.get('https://www.instagram.com/pinedah_11')

input("Press enter to quit")

browser.quit()