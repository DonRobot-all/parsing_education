import requests
import csv
from bs4 import BeautifulSoup

url = 'https://parsinger.ru/html/index4_page_{number}.html'

with open('collect_HDD.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=' ')
    writer.writerow([
        '​​​​​​​Наименование', 'Бренд', 'Форм-фактор',
        'Ёмкость', 'Объем буферной памяти', 'Цена'
        ])

responce = requests.get(url=url.format(number=1))
soup = BeautifulSoup(responce.text, 'html.parser')
last_page = int(soup.find('div', class_='pagen').text[-2]) + 1
for page in range(1, last_page):
    responce = requests.get(url=url.format(number=page))
    responce.encoding = 'utf-8'
    soup = BeautifulSoup(responce.text, 'html.parser')
    name = soup.find_all('div', class_='img_box')
    print(name[0].find_all('a', class_='name_item'))
    brand = ...
    form_factor = ...
    container = ...
    buffer_memory = ...
    cost = ...
