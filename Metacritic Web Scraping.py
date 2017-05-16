# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 00:41:57 2017

@author: RudradeepGuha
"""

import bs4
import requests

url = "http://www.metacritic.com/browse/tv/title/all"
counter = 96

def scrapePage(url, counter):
    
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
    tvShows = requests.get(url, headers = headers)
    tvShows.raise_for_status()
    tvShowSoup = bs4.BeautifulSoup(tvShows.text)

    shows = tvShowSoup.find_all("div", attrs = {'class' : "product_wrap"})

    for show in shows:
        if ((show.find(class_ = 'metascore_w small season positive') != None) and (show.find('span', class_ = "data textscore textscore_outstanding")) != None) and ((int(show.find(class_ = 'metascore_w small season positive').contents[0])) > 80):
                print(show.find('div', class_ = 'metascore_w small season positive').contents[0]
                      + " " + show.find('a').contents[0] 
                    + " " + show.find('span', class_ = "data textscore textscore_outstanding").contents[0])
                   
    midrl = tvShowSoup.find('span', class_ = "flipper next")
    
    if (midrl != None) and (midrl.find('a') != None):
        url = "http://www.metacritic.com" + midrl.find('a')['href']
        scrapePage(url, counter)
    else:
        if (chr(counter) != 'z'):
            counter = counter + 1
            midrl = tvShowSoup.find('li', class_ = "letter tab_" + chr(counter))
            url = "http://www.metacritic.com" + midrl.find('a')['href']
            scrapePage(url, counter)
        else:
            print("Done")
  
scrapePage(url, counter)