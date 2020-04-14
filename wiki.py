print("Exracting wiki page..... ")

import pandas as pd
import urllib.request
from bs4 import BeautifulSoup

import geopy
from geopy.geocoders import Nominatim


#Wikipedia website link

url = "https://en.wikipedia.org/wiki/List_of_motorcycle_manufacturers"
print("wiki page: " + str(url))
country_bike = {}

page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, "lxml")

# Extraction and save country and in dictionary

for x in soup.find_all('h3'):

    if hasattr(x.findChild("span"), 'id'):

        country = str(x.findChild("span")['id'])  # + str("_country")
        company = []
        for li in x.findNextSibling():
            company.append(li.find_next('a')['title'])

        company = list(set(company))
        country_bike[country] = company

    else:
        break

print("Bike companies of India:" + str(country_bike['India']))

print()