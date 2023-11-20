import requests
from bs4 import BeautifulSoup

url = 'https://parsinger.ru/html/hdd/4/4_1.html'
responce = requests.get(url=url)
responce.encoding = 'utf-8'
soup = BeautifulSoup(responce.text, 'html.parser')
current_price = int(soup.find('span', id='price').text.split()[0])
last_price = int(soup.find('span', id='old_price').text.split()[0])
print(round((last_price - current_price) / last_price * 100, 1))