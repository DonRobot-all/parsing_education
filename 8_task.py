import requests

# Ваш API-ключ от OpenWeather (замените на реальный ключ)
api_key = "ВАШ_API_КЛЮЧ"

# Город, для которого мы хотим получить погодные данные
city = "Москва"

# Словарь параметров для передачи в API
params = {
    'q': city,        # Название города
    'appid': api_key, # Ваш API-ключ
    'units': 'metric' # Единицы измерения (опционально)
}

# Базовый URL API сервиса погоды
base_url = "http://api.openweathermap.org/data/2.5/weather"

# Отправляем GET-запрос к API
response = requests.get(base_url, params=params)

# Проверяем статус ответа
if response.status_code == 200:
    # Выводим полученные данные о погоде
    print("Погодные данные для города {}: ".format(city))
    print(response.json())
else:
    # Выводим сообщение об ошибке
    print("Не удалось получить данные. Код ошибки: {}".format(response.status_code))