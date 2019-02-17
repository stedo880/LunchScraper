import pandas as pd
import numpy as np
import bs4
import re

from urllib.request import urlopen
from bs4 import BeautifulSoup

def main():
    scrape_mk()
    scrape_chili()

def scrape_mk():

    url = "http://www.matkultur.net/"
    html = urlopen(url)

    soup = BeautifulSoup    (html, 'lxml')

    #find the starting point
    soup_element = soup.find(text=re.compile("^Dagens")).findNext('p').findNext('p')

    #init lunch list
    lunch_mk = []

    for i in range(0, 16):
        lunch_mk.append(soup_element.text)
        soup_element = soup_element.findNext('p')

    print(lunch_mk)

def scrape_chili():

    url = "http://www.chili-lime.se/"
    html = urlopen(url)

    soup = BeautifulSoup(html, 'lxml')

    # find the starting point
    soup_element = soup.find(text=re.compile("^Dagens")).findNext('p').findNext('tr')

    # init lunch list
    lunch_chili = []

    for i in range(0, 16):
        #print(soup_element.text)
        lunch_chili.append(soup_element.text)
        soup_element = soup_element.findNext('p')

    print(lunch_chili)

if __name__ == '__main__':
    main()