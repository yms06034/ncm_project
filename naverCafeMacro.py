from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup as BS

import pandas as pd
import numpy as np
import time
import requests

def css_finds(css_selector):
    return driver.find_elements(By.CSS_SELECTOR, css_selector)

def css_find(css_selector):
    return driver.find_element(By.CSS_SELECTOR, css_selector)

def find(wait, css_selector):
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))

def finds_xpath(xpath):
    return driver.find_elements(By.XPATH, xpath)

def find_xpath(xpath):
    return driver.find_element(By.XPATH, xpath)

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--start-maximized')
options.add_argument('incognito')

# driver = webdriver.Chrome("./chromedriver.exe", options=options)
# wait = WebDriverWait(driver, 10)

URL = "https://naver.com"

# driver.get(URL) # naverCafe URL

response = requests.get(URL)
soup = BS(response.content, "html.parser")
print(soup.contents)
