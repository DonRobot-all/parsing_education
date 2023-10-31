# Импорт библиотеки
import requests

# Параметры запроса: ищем книги по программированию
params = {'text': 'DonRobot'}

# Отправка запроса
response = requests.get('https://yandex.ru/search/', params=params)

# Вывод результатов
print(response.text)


# https://yandex.ru/search/?text=DonRobot