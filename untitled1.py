# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 20:01:56 2021

@author: USER
"""

import requests
from bs4 import BeautifulSoup
with open('school.csv','w',encoding=("UTF-8")) as fobj:
            fobj.write('學校,地址,電話,網址\n')
for i in range(1,9):
    my_url = "https://highschool.yjvs.chc.edu.tw/search/index.php"
    param = {"city":9}
    param["page"]=i
    data = requests.get(my_url,params=param)
    data.encoding = "UTF-8"
    data = data.text
    results = BeautifulSoup(data,"html.parser")
    schools = results.find(id="school-list").find_all('table')
    for n in schools:
        items = n.find_all("li")
        with open("school.csv",'a',encoding=("UTF-8")) as f:
            f.write("{},{},{},{}\n".format(items[0].text,items[1].text,items[2].text,items[3].text))
        print(items[0].text,items[1].text,items[2].text,items[3].text,end="\n")