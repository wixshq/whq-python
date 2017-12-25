# -*- coding:utf-8 -*-
from selenium import webdriver
import os
import requests

def getLengthNumber(num,length):
    num_len = length - len(str(num))
    result = ""
    for k in range(num_len):
        result+="0"
    result+=str(num)
    return result


if __name__ == '__main__':
    chapter_url = "http://www.dangniao.com/mh/22996/"
    browser = webdriver.PhantomJS("/usr/local/mysoft/phantomjs-2.1.1/bin/phantomjs")
    browser.get(chapter_url)
    chapter_list = browser.find_elements_by_css_selector(".ksdjjjqwekjbkask23k a")
    chapters = []
    for chapter in chapter_list:
        title = chapter.get_attribute("title")
        href = chapter.get_attribute("href")
        item = []
        item.append(title)
        item.append(href)
        chapters.append(item)
    for item in chapters:
        title = item[0]
        print (title)
        dirpath = "./download/"+title
        if not os.path.exists(dirpath):
            os.makedirs(dirpath)
        href = item[1]
        browser.get(href)
        page = int(browser.find_element_by_id("dhtj").find_elements_by_tag_name("a")[-1].text)
        for i in range(page):
            src = browser.find_element_by_css_selector("#wdwailian img").get_attribute("src")
            print (src)
            name = dirpath+"/"+getLengthNumber(i+1,2)+".jpg"
            if not os.path.exists(name):
                with open(name,"wb") as code:
                    code.write(requests.get(src).content)
                print (name)
            if i!=page-1:
                browser.find_element_by_class_name("zsxiaye").click()