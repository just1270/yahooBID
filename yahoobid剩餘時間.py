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
driver.get("https://tw.bid.yahoo.com/search/auction/product?acu=2&p=us3c&refine=bidding&sort=etime")   #&sort=-ptime 最新上架排序 &sort=etime 剩餘時間
print(driver.title)
soup = BeautifulSoup(driver.page_source, "lxml")
tag_names = soup.find_all("span", class_="sc-dlGagL sc-gKBqHi sc-1drl28c-5 gkgFep iSWDmq hnGvZF") #商品名稱
target_prices = soup.find_all("span", class_="sc-dlGagL sc-gKBqHi dkipYY cWhwYS")                 #價格
target_hr = soup.find_all("span", class_="sc-dlGagL iotmEd")        #時
#target_min = soup.find_all("span", class_="sc-1w447g0-0 qOhjp")      #分
                                                                                    #剩餘時間
 
for tag_name, target_price, target_hr  in zip(tag_names, target_prices, target_hr):
    print("商品名稱:", tag_name.text)
    print("價格:", target_price.text)
    print("剩餘時間:", target_hr.text )
    print("-" * 50)                  #分隔線   

    
#點子3C
print("點子3C")
driver.get("https://tw.bid.yahoo.com/search/auction/product?acu=2&p=點子3C&refine=bidding&sort=etime")  #&sort=-ptime 最新上架排序
print(driver.title)
soup = BeautifulSoup(driver.page_source, "lxml")
tag_names = soup.find_all("span", class_="sc-dlGagL sc-gKBqHi sc-1drl28c-5 gkgFep iSWDmq hnGvZF") #商品名稱
target_prices = soup.find_all("span", class_="sc-dlGagL sc-gKBqHi dkipYY cWhwYS")                 #價格
target_hr = soup.find_all("span", class_="sc-dlGagL iotmEd")        #時
#target_min = soup.find_all("span", class_="sc-1w447g0-0 qOhjp")      #分
                                                                                    #剩餘時間
 
for tag_name, target_price, target_hr  in zip(tag_names, target_prices, target_hr):
    print("商品名稱:", tag_name.text)
    print("價格:", target_price.text)
    print("剩餘時間:", target_hr.text )
    print("-" * 50)               #分隔線


driver.quit()
