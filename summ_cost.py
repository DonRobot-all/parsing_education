import requests
from bs4 import BeautifulSoup

# url = 'https://dolinatsvetov.ru/tovary/mestnye-rozy-po-odnoy/'
url = 'https://rostov-na-donu.sushi-market.com/'
response = requests.get(url=url)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)
# price_flowers = soup.find_all('span', class_='p-price')
price_flowers = soup.find_all('meta', itemprop='price')
print(price_flowers)
# for price in price_flowers:
#     print(price.text.split()[1], price.text.split()[2])