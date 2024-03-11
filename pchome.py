from urllib import request
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.request import urlopen
from urllib.error import HTTPError
import re
import sqlite3
from selenium import webdriver
import json
import requests

def pchomeinfo():
    global pchomesearch

    res =requests.get(pchomesearch)
    ress = res.text

    jd = json.loads(ress)
    pcitems=[]
    pcprices=[]
    pcurls=[]
    pcmainurl='https://24h.pchome.com.tw/prod'
    try:

        for item in jd['prods']:
            pcitems.append(item['name'])
            pcprices.append(item['price'])
            url=pcmainurl+item['Id']
            pcurls.append(url)
        pcitems0 =pcitems[0]
        pcprices0 =pcprices[0]
        pcurls0 =pcurls[0]


    except:
        pcitems0 = "找不到資料"
        pcprices0 = "找不到資料"
        pcurls0 = "找不到資料"
    pcmatch(pcitems0)
    print(pcitems0)
    print(pcprices0)
    print(pcurls0)




