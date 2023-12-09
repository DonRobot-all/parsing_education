import requests
from bs4 import BeautifulSoup

url = 'https://parsinger.ru/html/index3_page_1.html'
first_side = 'https://parsinger.ru/html/'
response = requests.get(url=url)
soup = BeautifulSoup(response.text, 'html.parser')
pagination = soup.find('div', class_='pagen').find_all('a')
pages = [f"{first_side}{page['href']}" for page in pagination]
total = []
for page in pages:
    response = requests.get(url=page)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    things_on_page = soup.find_all('a', class_='name_item')
    total.append([things.text for things in things_on_page])

print(total)


# pages_one = requests.get(url=url)
# soup = BeautifulSoup(pages_one.text, 'html.parser')
# pagination = soup.find('div', class_='img_box').find_all('a')
# print(pagination)