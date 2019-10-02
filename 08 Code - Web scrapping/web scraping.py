# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 13:25:56 2019

@author: jose
"""

from bs4 import BeautifulSoup
html = '<p>Hello, world!</p> <p>Hello again.</p>'
soup = BeautifulSoup(html, 'lxml') # lxml is a html parser BS uses
#print(soup.text)

soup.find("p")

paragraphs = soup.find_all("p")
type(paragraphs)
first = paragraphs[0]
first.name
first.text
type(first)

import requests
r = requests.get('http://www.example.com')

type(r)
r.ok # When you request get it might not work, thi could return false
r.text
soup = BeautifulSoup(r.text, 'lxml') # lxml is a html parser BS uses

links = soup.find_all("a")

links[0].attrs #This gives me the dictionary of all the links
links[0].attrs["href"]

r = requests.get('http://www.theguardian.com')
soup = BeautifulSoup(r.text, 'lxml') # lxml is a html parser BS uses

soup.find_all("a")