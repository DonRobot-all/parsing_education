import requests
from bs4 import BeautifulSoup

url = 'https://parsinger.ru/4.3/4/index.html'

response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')


def sum_even_length_ids(soup):
    articuls = soup.find_all('p')
    total_id_sum, total_class_sum = 0, 0
    for string in articuls:
        if len(string.text.replace(' ', '')) % 2 == 0:
            total_id_sum += int(string.get('id'))
            total_class_sum += int(string.get('class')[0])
    return print(f"Сумма ID и CLASS тегов <p> с чётной длиной текста без пробелов: {total_id_sum + total_class_sum}")


sum_even_length_ids(soup)
