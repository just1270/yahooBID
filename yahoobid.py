from urllib import request
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.request import urlopen
from urllib.error import HTTPError
import re
import sqlite3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import json
import requests

#US3C
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://tw.bid.yahoo.com/search/auction/product?p=US3C&sort=-ptime")   #&sort=-ptime 最新上架排序
print(driver.title)
soup = BeautifulSoup(driver.page_source, "lxml")
tag_names = soup.find_all("span", class_="sc-dlGagL sc-gKBqHi sc-1drl28c-5 gkgFep iSWDmq hnGvZF")
target_prices = soup.find_all("span", class_="sc-dlGagL sc-gKBqHi dkipYY cWhwYS")
for tag_name, target_price in zip(tag_names, target_prices):
    print("商品名稱:", tag_name.text)
    print("價格:", target_price.text)
    print("-" * 50)       

    
#點子3C
print("點子3C")
driver.get("https://tw.bid.yahoo.com/search/auction/product?p=點子3C&sort=-ptime")  #&sort=-ptime 最新上架排序
print(driver.title)
soup = BeautifulSoup(driver.page_source, "lxml")
tag_names = soup.find_all("span", class_="sc-dlGagL sc-gKBqHi sc-1drl28c-5 gkgFep iSWDmq hnGvZF")
target_prices = soup.find_all("span", class_="sc-dlGagL sc-gKBqHi dkipYY cWhwYS")

for tag_name, target_price in zip(tag_names, target_prices):
    print("商品名稱:", tag_name.text)
    print("價格:", target_price.text)
    print("-" * 50)                     #分隔線


driver.quit()
