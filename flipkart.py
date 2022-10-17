import time
import requests
import os.path
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

## Setup chrome options
chrome_options = Options()
# chrome_options.add_argument("--headless") # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument('--disable-dev-shm-usage')
homedir = os.path.expanduser("~")

webdriver_service = Service(f"{homedir}/chromedriver/stable/chromedriver")

#webdriver_service = Service('/mnt/c/Users/babuk/chromedriver.exe')
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)
driver.maximize_window()
url = ('https://www.flipkart.com/')

driver.get(url)
time.sleep(15)
html = driver.page_source
soup = BeautifulSoup(html, "lxml")  
a = soup.find('div', {'class':"eFQ30H"}).text
time.sleep(20)

for a in soup.find_all('a', href=True):
    print(a['href'])

    

# for i in details:
#     print(details)
#     test = i.find()


