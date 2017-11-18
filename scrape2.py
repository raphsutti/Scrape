import requests, bs4

response = requests.get('http://www.te.com/usa-en/product-1-1418390-1.html')
soup = bs4.BeautifulSoup(response.text)

prodNum = soup.select('div.right-content-column h1')
prodNum = prodNum[0].get_text()
print(prodNum)

price = soup.select('ul.priceList li')
price = price[0].get_text()
print(price)