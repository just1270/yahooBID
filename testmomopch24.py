#來源:https://ivanjo39191.pixnet.net/blog/post/81852030-python-%E7%88%AC%E8%9F%B2%E7%B7%B4%E7%BF%92%E7%B4%80%E9%8C%842%28%E4%BA%8C%29
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


def productsearch(main):
    global momosearch
    global pchomesearch
    global yahoosearch
    global shpsearch
    global itemname

    str(main)
    momo = 'https://www.momoshop.com.tw/search/searchShop.jsp?keyword='
    momosearch = momo+main
    pchome = 'https://24h.pchome.com.tw/search/?q='
    pchomesearch = pchome+main
    yahoo = 'https://tw.bid.yahoo.com/search/auction/product?p='
    yahoosearch = yahoo+main
    shp1 = 'https://shopee.tw/search?keyword='
    #shp2 = '&sortBy=slae'
    shpsearch = shp1+main    #+shp2
    print("momo購物網:")
    print(momosearch)
    momoinfo()  
    print("Pchome24H購物:")  
    print(pchomesearch)
    pchomeinfo()
    print("yahoo拍賣:")
    print(yahoosearch)
    yahooinfo()
    print("蝦皮拍賣:")
    print(shpsearch)
    shpinfo()






