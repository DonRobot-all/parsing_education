import requests
from bs4 import BeautifulSoup

url = 'https://parsinger.ru/html/index3_page_1.html'
first_side = 'https://parsinger.ru/html/'
response = requests.get(url=url)
soup = BeautifulSoup(response.text, 'html.parser')
pagination = soup.find('div', class_='pagen').find_all('a')
print(pagination)
pages = [f"{first_side}{page['href']}" for page in pagination]
print(pages)

pages_one = requests.get(url=url)
soup = BeautifulSoup(pages_one.text, 'html.parser')
pagination = soup.find('div', class_='img_box').find_all('a')
print(pagination)