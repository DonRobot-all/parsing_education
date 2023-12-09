import requests
from bs4 import BeautifulSoup

total_categories = 5

url = 'https://parsinger.ru/html/index{categories}_page_{page}.html'

for category in range(1, total_categories):
    response = requests.get(url=url.format(categories=category, page=1))
    soup = BeautifulSoup(response.text, 'html.parser')
    pagination = int(soup.find_all('div', class_='pagen')[0].text[-2])
    for page in range(1, pagination):
        response = requests.get(url=url.format(categories=category, page=page))
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        cost = soup.find_all('p', class_='price')
        print(cost)
