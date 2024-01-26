import requests

url = 'https://jsonplaceholder.typicode.com/posts'
url = 'https://catalog.wb.ru/catalog/electronic22/catalog?TestGroup=no_test&TestID=no_test&appType=1&curr=rub&dest=-2227024&page=1&sort=popular&spp=27&subject=517'

response = requests.get(url=url).json()
thing = response['data']['products'][0]
print(thing['name'], thing['priceU'])