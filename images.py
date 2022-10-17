from distutils.filelist import findall
from heapq import merge
import time
from numpy import place
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


driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)
driver.maximize_window()
url = ('https://www.airbnb.co.in/')

driver.get(url)
time.sleep(20)

html = driver.page_source
soup = BeautifulSoup(html, "lxml")  
places = []

overall = soup.findAll('div', {'class': "g1qv1ctd cb4nyux dir dir-ltr"})
temp = []
for each in overall:
    s={}
    s['Destination'] = each.find('div', {'class': "t1jojoys dir dir-ltr"}).text
    site = each.findAll('div', {'class': "f15liw5s s1cjsi4j dir dir-ltr"})
    s['Visiting place'] = site[0].text 
    s['Available dates'] = site[1].text 
    s['Amount'] = each.find('span', {'class': "a8jt5op dir dir-ltr"}).text
    s['Rating'] = each.find('span', {'class': "r1dxllyb dir dir-ltr"}).text
    temp.append(s)
import pandas as pd
print(pd.DataFrame(temp)) 


driver.quit()
