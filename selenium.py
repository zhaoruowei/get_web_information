__author__ = 'zhaoruowei'
#! /usr/env python
#-*-coding:utf-8-*-

import time
import re
import os
import shutil
import sys
import codecs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.action_chains import ActionChains

#Open PhantomJS
driver = webdriver.Firefox(executable_path = '/Library/Python/2.7/site-packages/geckodriver')
driver2 = webdriver.PhantomJS(executable_path="/Library/Python/2.7/site-packages/phantomjs-2.1.1-macosx/bin/phantomjs")
wait = ui.WebDriverWait(driver,10)

def getAbstract(num,title,url):
    try:
        fileName = "/Users/zhaoruowei/Downloads/" + str(num) + ".txt"
        #result = open(fileName,"w")
        #Error: 'ascii' codec can't encode character u'\u223c'
        result = codecs.open(fileName,'w','utf-8')
        result.write("[Title]\r\n")
        result.write(title+"\r\n\r\n")
        result.write("[Auths]\r\n")
        driver2.get(url)
        elem = driver2.find_element_by_xpath("//div[@class='auths']")
        #print elem.text
        result.write(elem.text+"\r\n")
    except Exception,e:
        print 'Error:',e
    finally:
        result.close()
        print 'END\n'

def getURL():
    page = 1
    count = 1
    url_page = "https://www.ncbi.nlm.nih.gov/pubmed/?term=nature+communications"
    while page<=615:
        url_page = "https://www.ncbi.nlm.nih.gov/pubmed/?term=nature+communications"
        print url_page
        driver.get(url_page)
        elem_url = driver.find_elements_by_xpath("//p[@class='title']/a")
        for url in elem_url:
            num = "%05d" % count
            title = url.text
            url_content = url.get_attribute("href")
            print num
            print title
            print url_content
            getAbstract(num,title,url_content)
            count = count + 1
        else:
            print "Over Page " + str(page) + "\n\n"
        page = page + 1
    else:
        "Over getUrl()\n"
        time.sleep(5)

if __name__ == '__main__':
    '''
    path = "/Users/zhaoruowei/Downloads/"
    if os.path.isfile(path):         #Delete file
        os.remove(path)
    elif os.path.isdir(path):        #Delete dir
        shutil.rmtree(path, True)
    os.makedirs(path)                #Create the file directory
    '''
    getURL()
    print "Download has finished."
