import requests

url_new = 'https://parsinger.ru/3.3/1/{number}.html'


def search():
    for i in range(0, 200):
        if (response := s.get(url=url_new.format(number=i)).status_code) == 200:
            return response.text


with requests.Session() as s:
    s.get(url_new)
    print(search())
