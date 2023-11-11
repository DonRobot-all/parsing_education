from bs4 import BeautifulSoup

html = """
<html>
    <body>
        <h1>Заголовок 1</h1>
        <p class="text-class">Текст 1</p>
        <p class="text-class">Текст 2</p>
        <p id="text-id">Текст 3</p>
    </body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

# Найти все теги `p`
result = soup.find_all('p')
for tag in result:
    print(tag.text)

print('----разделитель----')

# Найти все теги `p` с атрибутом class='text-class'
result = soup.find_all('p', attrs={'class': 'text-class'})
for tag in result:
    print(tag.text)

print('----разделитель----')

# Найти все теги `p` с атрибутом id='text-id'
result = soup.find_all('p', attrs={'id': 'text-id'})
for tag in result:
    print(tag.text)