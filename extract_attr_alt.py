from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
</head>
<body>

<div class="card">
    <h2>Товар 1</h2>
    <img src="parsing.png" alt="779966">
    <p>Цена: 1000 руб.</p>
    <p>Описание: Отличный товар, изготовлен из качественных материалов.</p>
    <p>Технические характеристики: Размеры: 10x10x10 см, Вес: 1 кг.</p>
    <p>Доступные размеры: S, M, L</p>
    <p>Отзывы: 5 звезд</p>
    <p>Наличие на складе: В наличии</p>
    <p>Информация о доставке: Бесплатно при заказе от 3000 руб.</p>
    <a href="https://stepik.org/a/104774" class="btn">Купить</a>
</div>

<div class="card">
    <h2>Товар 2</h2>
    <img src="async.png" alt="331155">
    <p>Цена: 1500 руб.</p>
    <p>Описание: Превосходный товар, подходит для повседневного использования.</p>
    <p>Технические характеристики: Размеры: 15x15x15 см, Вес: 1.5 кг.</p>
    <p>Доступные размеры: M, L, XL</p>
    <p>Отзывы: 4.5 звезд</p>
    <p>Наличие на складе: В наличии</p>
    <p>Информация о доставке: Бесплатно при заказе от 5000 руб.</p>
    <a href="https://stepik.org/a/170777" class="btn">Купить</a>
</div>

<div class="card">
    <h2>Товар 3</h2>
    <img src="parsing.png" alt="558877">
    <p>Цена: 2000 руб.</p>
    <p>Описание: Удобный товар для дома и офиса.</p>
    <p>Технические характеристики: Размеры: 12x12x12 см, Вес: 1.2 кг.</p>
    <p>Доступные размеры: S, M</p>
    <p>Отзывы: 4.7 звезд</p>
    <p>Наличие на складе: В наличии</p>
    <p>Информация о доставке: Бесплатно при заказе от 3500 руб.</p>
    <a href="https://stepik.org/a/104774" class="btn">Купить</a>
</div>

<div class="card">
    <h2>Товар 4</h2>
    <img src="async.png" alt="449933">
    <p>Цена: 2500 руб.</p>
    <p>Описание: Стильный и практичный товар.</p>
    <p>Технические характеристики: Размеры: 14x14x14 см, Вес: 1.4 кг.</p>
    <p>Доступные размеры: L, XL</p>
    <p>Отзывы: 4.8 звезд</p>
    <p>Наличие на складе: В наличии</p>
    <p>Информация о доставке: Бесплатно при заказе от 4000 руб.</p>
    <a href="https://stepik.org/a/170777" class="btn">Купить</a>
</div>

<div class="card">
    <h2>Товар 5</h2>
    <img src="parsing.png" alt="667711">
    <p>Цена: 2700 руб.</p>
    <p>Описание: Идеальный товар для повседневного использования.</p>
    <p>Технические характеристики: Размеры: 13x13x13 см, Вес: 1.3 кг.</p>
    <p>Доступные размеры: M, L, XL</p>
    <p>Отзывы: 4.9 звезд</p>
    <p>Наличие на складе: В наличии</p>
    <p>Информация о доставке: Бесплатно при заказе от 4500 руб.</p>
    <a href="https://stepik.org/a/104774" class="btn">Купить</a>
</div>

<div class="card">
    <h2>Товар 6</h2>
    <img src="async.png" alt="334455">
    <p>Цена: 3000 руб.</p>
    <p>Описание: Прочный и надежный товар.</p>
    <p>Технические характеристики: Размеры: 16x16x16 см, Вес: 1.6 кг.</p>
    <p>Доступные размеры: S, M</p>
    <p>Отзывы: 5 звезд</p>
    <p>Наличие на складе: В наличии</p>
    <p>Информация о доставке: Бесплатно при заказе от 5000 руб.</p>
    <a href="https://stepik.org/a/170777" class="btn">Купить</a>
</div>


</body>
</html>
"""


def main():
    soup = BeautifulSoup(html_doc, 'html.parser')
    img_tags = soup.find_all('img')
    total_sum = sum(int(img_tag.get('alt')) for img_tag in img_tags)
    print(f"Сумма всех значений в атрибуте alt тега img: {total_sum}")


main()
