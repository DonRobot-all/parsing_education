from bs4 import BeautifulSoup


html = open('index.html', encoding='utf-8')
soup = BeautifulSoup(html, 'html.parser')
html.close()
tag = soup.div

print(soup)