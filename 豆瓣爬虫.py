#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 10:56:17 2018

@author: lidawei
"""
import requests, re, time
from bs4 import BeautifulSoup

count = 0
i =0
sum, count_s = 0, 0 
while(count < 50):
    try:
        #抓取
        r = requests.get('https://book.douban.com/subject/1477390/comments/hot?p=' + str(i+1))
    except Exception as err: 
        print(err)
        break
    #解析
    soup = BeautifulSoup(r.text, 'lxml')
    comments = soup.find_all('p', 'comment-content') 
    for item in comments:
        count = count + 1  
        print(count, item.string) 
        if count == 50: 
            break
    pattern = re.compile('<span class="user-stars allstar(.*?) rating"') 
    p = re.findall(pattern, r.text)
    #计算评分总和
    for star in p:
        count_s = count_s + 1
        sum += int(star)
    time.sleep(5) 
if count == 50:
    #评分是50分制，打星是五分制，所以再除以十
    print(sum / count_s / 10)
