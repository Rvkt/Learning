# -*- coding: utf-8 -*-
"""Web Scraping.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uM8qmBlf2pnd8zUFLOgnQYq7_IXHilFm

# **Editorial of The Hindu**
"""

import requests
from bs4 import BeautifulSoup as bs

r = requests.get('https://www.thehindu.com/opinion/')

soup = bs(r.content)

# print(soup.prettify())

# get the links of the editorial
for link in soup.find_all('a', class_='ES2-100x4-text1-heading'):
    print(link.get('href'))

import requests
from bs4 import BeautifulSoup as bs

r = requests.get('https://www.thehindu.com/todays-paper/')

soup = bs(r.content)

# print(soup.prettify())

# get the links
for a in soup.find_all('a'):
    print(a.get('href'))

import requests
from bs4 import BeautifulSoup as bs

r = requests.get('https://www.thehindu.com/news/national/')

soup = bs(r.content)

# print(soup.prettify())

for div in soup.find_all('div', class_='story-card-news'):
    print(div.getText())

import requests
from bs4 import BeautifulSoup as bs

r = requests.get('https://www.gktoday.in/topic/current-affairs-todays-headlines-january-1/')

soup = bs(r.content)

# print(soup.prettify())

# get the links of the editorial
for p in soup.find_all('p'):
    print(p.getText())