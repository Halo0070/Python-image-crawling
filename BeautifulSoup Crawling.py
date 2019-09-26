import requests
import urllib.request
import urllib.parse
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

        if not duplicate(save_image):
            urllib.request.urlretrieve(url, "./img/" + save_image)
        else:
            print("중복된 이미지!")
 
def save_image(fullurl,url):
    print(fullurl,"   ",url)
    print(url.find('http')==-1 and url.find('www')==-1)
    print('->',url)
    if url.find('http')==-1 and url.find('www')==-1:                #if = -1 (not find)
        url = fullurl+url
        print('-<',url)
    a_code = requests.get(url)

    pathFileName = os.path.join('D:/Crawling Image',url[-9:-3]+'.png')
    urllib.request.urlretrieve(url, pathFileName)
    urllib.request.urlretrieve(url, a_code) #
    
    pathFileName.request.urlretrieve(urllib) #
    
    for _ in range(500):
        pathFileName.execute_script("window.scrollBy(0,10000)")
        pathFileName.close()

# 중복 체크
def duplicate(img):
    return os.path.exists("./img/" + img)
        
        

    
    print('OK!')
main(1) #max page

