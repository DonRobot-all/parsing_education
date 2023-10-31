import requests

url = 'https://parsinger.ru/3.3/4/{number}.html'

with requests.Session() as s:
    for first_available_page in range(100):
        if s.get(url=url.format(number=first_available_page)).status_code == 200:
            break
    for last_available_page in range(100, 0, -1):        
        if s.get(url=url.format(number=last_available_page)).status_code == 200:
            break

print(f"Первая доступная страница: {first_available_page}.html")
print(f"Последняя доступная страница: {last_available_page}.html")