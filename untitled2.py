# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 21:11:48 2021

@author: USER
"""

import requests
from bs4 import BeautifulSoup
my_url = "https://www.irasutoya.com/2021/01/onepiece.html"
data = requests.get(my_url)
data.encoding = "UTF-8"
data = data.text
results = BeautifulSoup(data,"html.parser")
images = results.find_all("div",class_="floatimg")
i=1
for c in images:
    fileName = str(i)+'.png'
    imgs = c.find("img").get('src')
    pictures = requests.get(imgs)
    with open(fileName,"wb") as f:
        f.write(pictures.content)
    i += 1
    print(imgs)