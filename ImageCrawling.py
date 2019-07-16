from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import chrome
from bs4 import BeautifulSoup
import json
import os
import urllib3
import argparse

search = 'baseball' # 찾고자 하는 이미지 검색어
url = "https://www.google.com/search?q="+search+"&source=lnms&tbm=isch"
browser=webdriver.Chrome('D:/GitHub/Python image crawling/Python-image-crawling/chromedriver')
browser.get(url)
header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}

counter = 0
succounter = 0

print(os.path)

def get_soup(url,header):
    return BeautifulSoup(urllib3.urlopen(urllib3.Request(url,headers=header)),'html.parser')

def main(args):
    parser = argparse.ArgumentParser(description='Scrape Google images')
    parser.add_argument('-s', '--search', default='bananas', type=str, help='search term')
	parser.add_argument('-n', '--num_images', default=10, type=int, help='num images to save')


    for _ in range(500):
        browser.execute_script("window.scrollBy(0,10000)")
        browser.close()



