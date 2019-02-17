import pandas as pd
import numpy as np
import bs4
import re
import datetime

from urllib.request import urlopen
from bs4 import BeautifulSoup

def main():
    scrape_mk()
    #scrape_chili()
    scrape_p2()

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

def scrape_husman():

    url = "https://restauranghusman.se/"
    html = urlopen(url)

    soup = BeautifulSoup    (html, 'lxml')

    #find the starting point
    soup_element = soup.find(text=re.compile("^Dagens")).findNext('p').findNext('p')

    #init lunch list
    lunch_husman = []

    for i in range(0, 16):
        lunch_husman.append(soup_element.text)
        soup_element = soup_element.findNext('p')

    print(lunch_husman)

def scrape_collegium():

    url = "http://www.sodexomeetings.se/collegium/en/restaurang-och-cafe/lunchmeny/"
    html = urlopen(url)

    soup = BeautifulSoup    (html, 'lxml')

    #find the starting point
    soup_element = soup.find(text=re.compile("^Dagens")).findNext('p').findNext('p')

    #init lunch list
    lunch_collegium = []

    for i in range(0, 16):
        lunch_collegium.append(soup_element.text)
        soup_element = soup_element.findNext('p')

    print(lunch_collegium)

def scrape_p2():

    url = "https://p2catering.se/lunchmenyer/lunchmeny-vecka-" + str(datetime.datetime.now().isocalendar()[1]) + "-" + str(datetime.datetime.now().year) + "/"

    print(url)

    html = urlopen(url)

    soup = BeautifulSoup    (html, 'lxml')

    #find the starting point
    soup_element = soup.find(text=re.compile("^Dagens")).findNext('p').findNext('p')

    #init lunch list
    lunch_p2 = []

    for i in range(0, 16):
        lunch_p2.append(soup_element.text)
        soup_element = soup_element.findNext('p')

    print(lunch_p2)

if __name__ == '__main__':
    main()