import requests

url = 'https://parsinger.ru/img_download/img/ready/{number}.png'

response = requests.get(url=url)
print(response.text)

for i in range(161):
    with open(f'image{i}.jpeg', 'wb') as file:
        response = requests.get(url=url.format(number=i))
        file.write(response.content)