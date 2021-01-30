import requests
from bs4 import BeautifulSoup

# https://realpython.com/beautiful-soup-web-scraper-python/#why-scrape-the-web
# This website is great for getting started!

# GME stock
URL = 'https://finance.yahoo.com/quote/GME?.tsrc=applewf'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

# AMC stock
URL2 = 'https://finance.yahoo.com/quote/AMC?p=AMC&.tsrc=fin-srch'
page2 = requests.get(URL2)
soup2 = BeautifulSoup(page.content, 'html.parser')

# BB stock
URL3 = 'https://finance.yahoo.com/quote/BB?p=BB&.tsrc=fin-srch'
page3 = requests.get(URL3)
soup3 = BeautifulSoup(page.content, 'html.parser')


def stockInfoExtract(url, stockNum):
    URL = url
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Printing the source name
    arrayWeb = URL.split('/')
    arraySite = arrayWeb[2].split('.')
    siteName = arraySite[1] + " " + arraySite[0]

    # Saving the Ticker
    title = str(soup.find(class_='D(ib) Fz(18px)'))
    titlePt1 = title.split(">", 1)
    titlePt2 = titlePt1[1].split("<")
    finalTitle = titlePt2[0]

    # Saving the price value
    price = soup.find(class_='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)')
    priceStr = str(price)
    pricePt1 = priceStr.split(">", 1)
    pricePt2 = pricePt1[1].split("<")
    finalPrice = pricePt2[0]

    # Saving the after hour price value
    afterPrice = str(soup.find(class_="C($primaryColor) Fz(24px) Fw(b)"))
    afterPricePt1 = afterPrice.split(">", 1)
    afterPricePt2 = afterPricePt1[1].split("<")
    finalAfterPrice = afterPricePt2[0]

    # Output of our information
    print("########### Stock " + str(stockNum) + " ###########")
    print("SOURCE: " + siteName)
    print("COMPANY + TICKER: " + finalTitle)
    print("PRICE: " + "$" + finalPrice)
    print("AFTER HRS PRICE: " + "$" + finalAfterPrice)
    print("\n")



#### Welcome Note ####
print("####### Welcome to Stonk Viewer #######\n")
stockNum = 1
stockInfoExtract(URL, stockNum)
stockNum += 1
stockInfoExtract(URL2, stockNum)
stockNum += 1
stockInfoExtract(URL3, stockNum)

"""
print("########### Stock " + str(stockNum) + " ###########")
# Printing the source name
arrayWeb = URL.split('/')
arraySite = arrayWeb[2].split('.')
siteName = arraySite[1] + " " + arraySite[0]

# Saving the Ticker
title = str(soup.find(class_='D(ib) Fz(18px)'))
titlePt1 = title.split(">", 1)
titlePt2 = titlePt1[1].split("<")
finalTitle = titlePt2[0]

# Saving the price value
price = soup.find(class_='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)')
priceStr = str(price)
pricePt1 = priceStr.split(">", 1)
pricePt2 = pricePt1[1].split("<")
finalPrice = pricePt2[0]

# Saving the after hour price value
afterPrice = str(soup.find(class_="C($primaryColor) Fz(24px) Fw(b)"))
afterPricePt1 = afterPrice.split(">", 1)
afterPricePt2 = afterPricePt1[1].split("<")
finalAfterPrice = afterPricePt2[0]

# Increasing our stock num
stockNum += 1

# Output of our information
print("SOURCE: " + siteName)
print("COMPANY + TICKER: " + finalTitle)
print("PRICE: " + "$" + finalPrice)
print("AFTER HRS PRICE: " + "$" + finalAfterPrice)
"""
