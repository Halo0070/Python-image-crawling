import requests
import urllib.request
import json
import os
from bs4 import BeautifulSoup

def main(pages):
    page = 1
    while page <= pages:
        url = 'https://www.pinterest.co.kr/pin/755901118681775962/'
        a_code = requests.get(url)
        a_text = a_code.text
        soup = BeautifulSoup(a_text, 'html.parser')
        for link in soup.findAll('img', ):
            href = link.get('src')
            if href == None:
                print('Nothing')
                break
            else:
                save_image(url,href)
        page += 1
 
def save_image(fullurl,url):
    print(fullurl,"   ",url)
    print(url.find('http')==-1 and url.find('www')==-1)
    print('->',url)
    if url.find('http')==-1 and url.find('www')==-1:                #if = -1 (not find)
        url = fullurl+url
        print('-<',url)
    a_code = requests.get(url)
    pathFileName = os.path.join('D:/Crawling Image',url[-9:-3]+'.png')
    urllib.request.urlretrieve(url,pathFileName)

    for _ in range(500):
        pathFileName.execute_script("window.scrollBy(0,10000)")
        pathFileName.close()
    

    print('OK!')
main(1) #max page
