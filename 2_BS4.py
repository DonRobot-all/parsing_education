from bs4 import BeautifulSoup

html_doc = """
<html>
    <head>
        <title>Example Page</title>
    </head>
    <body>
        <h1>Hello World</h1>
        <p> First p without info </p>
        <p class="info">This is a paragraph.</p>
        <p class="info">This is another paragraph.</p>
    </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# Найдёт первый тег h1
first_h1 = soup.find('h1')
print(first_h1)

print('----разделитель----')

# Найдёт первый тег p с классом "info"
first_p = soup.find('p', {'class': 'info'})
print(first_p)

first_p_without_info = soup.find('p')
print(first_p_without_info)