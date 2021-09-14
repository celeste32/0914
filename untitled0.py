# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 19:41:43 2021

@author: USER
"""

import requests
from bs4 import BeautifulSoup
my_url = "https://www.ptt.cc/bbs/Gossiping/index.html"

for n in range(10):
    print("第{}頁".format(n+1))
    header = {"cookie":"over18=1"}
    data = requests.get(my_url,headers=header)
    data.encoding = "UTF-8"
    data = data.text
    
    results = BeautifulSoup(data,"html.parser")

    news = results.find_all("div",class_="r-ent")

    for i in news:
        print(i.find("div",class_="date").text, end=" ")
        print("https://www.ptt.cc"+i.a.get("href"),end=" ")
        print(i.a.text)


    my_url = "https://www.ptt.cc"+results.find_all("a",class_="btn wide")[1].get("href")