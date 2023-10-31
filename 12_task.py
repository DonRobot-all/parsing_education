import requests
from name_img import name_img

url = 'https://parsinger.ru/3.3/3/img/'

# with requests.Session() as s:
#     s.get(url)
#     max_size = 0
#     answer = ''
#     for name in name_img:
#         responce = s.get(f'{url}{name}')
#         size = int(responce.headers.get('Content-Length'))
#         if size > max_size:
#             max_size = size
#             answer = name
# print(answer)


with requests.Session() as s:
    answer = ''
    max_size = 0
    for name in name_img:
        if (max := int(s.get(f'{url}{name}').headers.get('Content-Length'))) > max_size:
            max_size, answer = max, name
print(answer)