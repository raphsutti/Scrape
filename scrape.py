#!/usr/bin/python3
# scrape.py
# written by Raph Suttiyotin 18/11/2017

from lxml import html
import requests

# provide an input file with list of marketing part numbers
file = open('input.txt', 'r')
prodList = file.read().splitlines()
filew = open('list.txt', 'w')
filew.write('Marketing Part Number,Description\n')
j = 1
for i in prodList:

    url = "https://www.te.com/usa-en/product-" + i + ".html"

    page = requests.get(url)
    tree = html.fromstring(page.content)

    description = tree.xpath('//h1[@class="product-name"]/text()')
    # print(description)

    partNumber = tree.xpath('//span[@class="mpn"]/text()')[0]

    print("Run: " + str(j))
    j +=1
    print('Found: ' + partNumber + ' - ' + description[0])

    filew.write(partNumber + ',' + description[0] +'\n')

filew.close()