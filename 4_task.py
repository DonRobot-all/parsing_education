import requests

# Определение заголовков, которые будут отправлены с запросом
headers = {
    'User-Agent': 'Mozilla/5.0',                  # Идентификация типа браузера, который отправляет запрос
    'Accept': 'text/html,application/xhtml+xml',  # Типы контента, которые клиент может обработать
    'Connection': 'keep-alive'                    # Указание на необходимость использования постоянного соединения
}

# Выполнение GET-запроса с установленными заголовками
response = requests.get('http://httpbin.org/user-agent', headers=headers)

print(response.text)