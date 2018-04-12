__author__ = 'zhaoruowei'
#! /usr/env python
#-*-coding:utf-8-*-

import urllib2
from BeautifulSoup import BeautifulSoup
import re

path_url_list = raw_input("url.txt path:")
path_out_list = raw_input("out.txt path:")

generef = open(path_url_list)
while True:
    ref = generef.readline()
    if not ref:
        break
    pass
    url = "https://www.ncbi.nlm.nih.gov/gene/?term=" + str(ref)
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html)
    title = soup.findAll('title')
    list = open(path_out_list,"a")
    list.write(str(title[0].contents[0])+'\r\n')
    print(str(title[0].contents[0]))
    list.close()
generef.close()
