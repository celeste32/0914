# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
from bs4 import BeautifulSoup
my_url = "https://www.ptt.cc/bbs/Food/index.html"

for n in range(10):
    print("第{}頁".format(n+1))

    data = requests.get(my_url)
    data.encoding = "UTF-8"
    data = data.text
    
    results = BeautifulSoup(data,"html.parser")

    foods = results.find_all("div",class_="r-ent")

    for i in foods:
        print(i.find("div",class_="date").text, end=" ")
        print("https://www.ptt.cc"+i.a.get("href"),end=" ")
        print(i.a.text)


    my_url = "https://www.ptt.cc"+results.find_all("a",class_="btn wide")[1].get("href")