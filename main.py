import pandas as pd
import numpy as np
import bs4
import re
import datetime

from urllib.request import urlopen
from bs4 import BeautifulSoup

def main():
    scrape_mjardevi()
    #scrape_mk()

def scrape_mjardevi():

    url = "https://mjardevi.se/lunch-menu/"
    html = urlopen(url)

    soup = BeautifulSoup    (html, 'lxml')

    #find all the juicy divs
    lunch_divs = soup.findAll("div", {"class": "lunch-menu-restaurant"})

    #init lunch list
    lunch_mjardevi = []

    for div in lunch_divs:
        lunch_mjardevi.append(div.text)

    for row in lunch_mjardevi:
        print(row + "\n")

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



if __name__ == '__main__':
    main()