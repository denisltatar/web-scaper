import requests
from bs4 import BeautifulSoup

# https://realpython.com/beautiful-soup-web-scraper-python/#why-scrape-the-web
# This website is great for getting started!

URL = 'https://finance.yahoo.com/quote/GME?.tsrc=applewf'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

# Saving the price value
price = soup.find(class_='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)')
newSplit = price.split('>')
print(newSplit)

# Saving the after hour price value
afterPrice = soup.find(class_='C($primaryColor) Fz(24px) Fw(b) cc_cursor')
# print(afterPrice.prettify())


# Printing the name of the website lol
arrayWeb = URL.split('/')
arraySite = arrayWeb[2].split('.')
siteName = arraySite[1] + " " + arraySite[0]


# Output of our information
print("This information is being printed from: " + siteName)
# print("PRICE: " + price)
# print("After hours: " + afterPrice)

        



