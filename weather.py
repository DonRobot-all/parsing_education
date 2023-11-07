import requests

url = 'https://parsinger.ru/3.4/1/json_weather.json'

response = requests.get(url=url)
answer = response.json()
temperature = int(answer[0]['Температура воздуха'].replace('°C', ''))
cold_day = answer[0]['Дата']
for day in answer:
    temperature_in_day = int(day['Температура воздуха'].replace('°C', ''))
    if temperature_in_day < temperature:
        temperature = temperature_in_day
        cold_day = day['Дата']

print(cold_day)

# # if(date := day['Дата'] for day in answer

# import requests

# URL = "https://parsinger.ru/3.4/1/json_weather.json"
# lst = requests.get(URL).json()
# sorted_lst = sorted(lst, key=lambda x: float(x['Температура воздуха'][:-2]))
# print(sorted_lst[0]['Дата'])



# import requests

# URL = "https://parsinger.ru/3.4/1/json_weather.json"
# lst = requests.get(URL).json()

# def sort_key(s):
#     return float(s['Температура воздуха'][:-2])

# sorted_lst = sorted(lst, key=sort_key)
# print(sorted_lst[0]['Дата'])