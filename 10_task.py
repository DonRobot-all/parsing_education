import requests

url = 'https://parsinger.ru/3.3/2/'
url_new = 'https://parsinger.ru/3.3/2/{number}.html'

with requests.Session() as s:
    s.get(url)
    # status = 0
    # for i in range(0, 200):
    #     response = s.get(url=url+str(i)+'.html')
    #     status += response.status_code
    status = sum(s.get(url=f'{url}{i}.html').status_code for i in range(0, 200))
    status_new = sum(s.get(url=url_new.format(number=i)).status_code for i in range(0, 200))
print(status)
print(status_new)
