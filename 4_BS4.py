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

# Найдите первый div с идентификатором «main»
main_div = soup.find('div', attrs={'id': 'main'})
print(main_div)

print('----разделитель----')

# Найдите первый тег p с классом "info"
info_p = soup.find('p', attrs={'class': 'info'})
print(info_p)