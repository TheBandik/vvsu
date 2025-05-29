# Скрапинг на Python с использованием requests и BeautifulSoup

Мы рассмотрим основные концепции и инструменты для выполнения скрапинга на Python. Мы будем использовать только базовые функции библиотек `requests` и `BeautifulSoup`.

## Что такое скрапинг?

**Скрапинг** — это процесс автоматического извлечения данных из страниц. С помощью Python можно загружать HTML-код страницы, анализировать его структуру и извлекать нужные данные.

### Применение скрапинга:

1. Сбор данных для анализа (например, цены товаров, отзывы, рейтинги)
2. Мониторинг изменений на сайте
3. Автоматизация рутинных задач (например, извлечение информации из таблиц)

## Этические аспекты

Прежде чем начать скрапинг, важно помнить:

- **Не перегружайте серверы** — делайте паузы между запросами
- **Соблюдайте законы** — не собирайте личные данные без разрешения

## Установка необходимых библиотек

Для выполнения скрапинга нам понадобятся две основные библиотеки:

```bash
pip install requests
pip install beautifulsoup4
```

## Основы работы с requests

Библиотека `requests` используется для отправки HTTP-запросов к сайтам и получения их содержимого.

### Простой GET-запрос

```python
import requests

url = 'https://example.com'
response = requests.get(url)

# Проверка успешности запроса
if response.status_code == 200:
    print("Страница успешно загружена")
    print(response.text)  # HTML-код страницы
else:
    print(f"Ошибка: {response.status_code}")
```

### Заголовки запроса (User-Agent)

Некоторые сайты блокируют запросы от скриптов. Чтобы избежать этого, можно указать заголовок `User-Agent`, который имитирует браузер.

```python
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)
print(response.text)
```

## Основы работы с BeautifulSoup

Библиотека `BeautifulSoup` используется для анализа HTML-кода и извлечения данных.

### Создание объекта BeautifulSoup

```python
from bs4 import BeautifulSoup

html_doc = """
&lt;html&gt;
  &lt;head&gt;&lt;title&gt;Пример&lt;/title&gt;&lt;/head&gt;
  &lt;body&gt;
    <p>Это пример текста.</p>
    <a href="https://example.com">Ссылка</a>
  &lt;/body&gt;
&lt;/html&gt;
"""

# Создание объекта BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

# Вывод HTML в структурированном виде
print(soup.prettify())
```

## Извлечение данных из HTML

### Поиск элементов

#### Метод `.find()`

Находит первый элемент по указанным критериям.

```python
# Найти первый тег <p>
p_tag = soup.find('p')
print(p_tag.text)  # Вывод текста внутри тега </p><p>
```

#### Метод `.find_all()`

Находит все элементы по указанным критериям.

```python
# Найти все теги <a>
a_tags = soup.find_all('a')
for tag in a_tags:
    print(tag['href'])  # Вывод значения атрибута href
```

#### Поиск по атрибутам

```python
# Найти элемент с определенным классом
content = soup.find('p', class_='content')
print(content.text)
```

#### CSS-селекторы с `.select()`

```python
# Найти элементы с помощью CSS-селекторов
links = soup.select('a')  # Все теги </a><a>
print([link['href'] for link in links])
```

## Практический пример: Скрапинг цитат с сайта quotes.toscrape.com

Мы будем извлекать цитаты, авторов и теги с сайта [quotes.toscrape.com](https://quotes.toscrape.com).

### Шаг 1: Загрузка страницы

```python
import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
else:
    print(f"Ошибка: {response.status_code}")
```


### Шаг 2: Извлечение данных

```python
# Найти все цитаты на странице
quotes = soup.find_all('div', class_='quote')

for quote in quotes:
    text = quote.find('span', class_='text').text  # Текст цитаты
    author = quote.find('small', class_='author').text  # Автор цитаты
    
    # Извлечение тегов цитаты
    tags = quote.find_all('a', class_='tag')
    tag_list = [tag.text for tag in tags]
    
    print(f"Цитата: {text}")
    print(f"Автор: {author}")
    print(f"Теги: {', '.join(tag_list)}")
    print('-' * 50)
```

## Сохранение данных в файл

После извлечения данных их можно сохранить в CSV-файл для дальнейшего использования.

### Сохранение в CSV

```python
import csv

data = [
    {'text': 'Цитата 1', 'author': 'Автор 1', 'tags': 'тег1, тег2'},
    {'text': 'Цитата 2', 'author': 'Автор 2', 'tags': 'тег3'}
]

with open('quotes.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['text', 'author', 'tags'])
    writer.writeheader()
    writer.writerows(data)

print("Данные сохранены в quotes.csv")
```

## Дополнительные техники скрапинга

### Обработка нескольких страниц (пагинация)

Многие сайты используют пагинацию для отображения данных на нескольких страницах. Чтобы скрапить такие сайты, нужно переходить по ссылкам на следующую страницу.

```python
url = 'https://quotes.toscrape.com/page/{}/'

page_num = 1
while True:
    response = requests.get(url.format(page_num))
    
    if response.status_code != 200:
        break
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    quotes = soup.find_all('div', class_='quote')
    if not quotes:
        break
    
    for quote in quotes:
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        
        tags = [tag.text for tag in quote.find_all('a', class_='tag')]
        print(f"Цитата: {text}, Автор: {author}, Теги: {tags}")
    
    page_num += 1

print("Скрапинг завершен")
```
