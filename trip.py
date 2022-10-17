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
url = ('https://dev.rentalforincome.com/property/list')

driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, "lxml")  




overall=soup.findAll('div',{'class':'box-footer'})
temp = []
for each in overall:
    r = {}
    r['test'] = each.find('h3',{'class':'proptitle'}).text
    case1 = each.findAll('strong')
    r['sector'] = case1[0].text
    r['sector1'] = case1[1].text

    temp.append(r)
print(temp)
import pandas as pd
print(pd.DataFrame(temp)) 


     


    
    


    




# import json
# print(json.dumps(hotels, indent =2))

driver.quit()