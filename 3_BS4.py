from bs4 import BeautifulSoup

html_doc = """
<html>
    <head>
        <title>Example Page</title>
    </head>
    <body>
        <div id="main">
            <h1>Hello World</h1>
            <p class="info">This is a paragraph.</p>
            <p class="info">This is another paragraph.</p>
            <ul>
                <li>Item 1</li>
                <li>Item 2</li>
                <li>Item 3</li>
            </ul>
        </div>
        <div id="secondary">
            <p>Some additional information.</p>
        </div>
    </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# Находим первый div с id "main"
main_div = soup.find('div', {'id': 'main'})
print(main_div)

print('----разделитель----')

# Найдите первый тег h1 внутри «основного» div
main_h1 = main_div.find('h1')
print(main_h1)

print('----разделитель----')

# Найдите первый тег p с классом «информация» внутри «основного» div
main_p = main_div.find('p', {'class': 'info'})
print(main_p)

print('----разделитель----')

# Найдите первый тег ul внутри «основного» div
main_ul = main_div.find('ul')
print(main_ul)