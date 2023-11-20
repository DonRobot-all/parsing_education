from bs4 import BeautifulSoup
import requests

url = 'https://parsinger.ru/html/index1_page_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')
all_watch = soup.findAll('p', class_='price')
total_sum = sum(int(number.text.split()[0]) for number in all_watch)
print(total_sum)
