# Работа с табличными данными в Python

## Установка и настройка окружения

Перед началом работы необходимо установить библиотеку `pandas` для работы с табличными данными.

```bash
pip install pandas
```

## Основы Pandas: DataFrame и Series

- **DataFrame** — это таблица с названиями столбцов и индексами строк.
- **Series** — это одномерный массив данных (аналог столбца в таблице).

Пример создания **DataFrame**: 

```python
data = {
    'Страна': ['Россия', 'США', 'Китай'],
    'ВВП (трлн $)': [2.1, 25.4, 17.8],
    'Инфляция (%)': [5.8, 3.2, 2.1]
}
df = pd.DataFrame(data)
print(df)
```

## Загрузка данных

### Загрузка из CSV

```python
df = pd.read_csv('data.csv')
```

### Загрузка из Excel

```python
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')
```

### Первичный анализ данных

Просмотр первых строк:

```python
print(df.head(5))  # Первые 5 строк
```

Общая информация:

```python
print(df.info())   # Типы данных и пропуски
```

Статистика по числовым данным:

```python
print(df.describe())
```

## Фильтрация данных

Фильтруем строки по условию:

```python
high_gdp = df[df['ВВП (трлн $)'] > 10]
print(high_gdp)
```

Используем логические операторы:

```python
filtered = df[(df['ВВП (трлн $)'] > 10) & (df['Инфляция (%)'] < 4)]
print(filtered)
```

## Сортировка данных

Сортируем данные по убыванию:

```python
sorted_df = df.sort_values(by='ВВП (трлн $)', ascending=False)
print(sorted_df)
```

## Агрегация данных

Группируем данные по региону и считаем средние значения:

```python
df['Регион'] = ['Европа', 'Америка', 'Азия']
grouped = df.groupby('Регион').mean()
print(grouped)
```

Создаём сводную таблицу:

```python
pivot = df.pivot_table(values='ВВП (трлн $)', index='Регион', aggfunc='sum')
print(pivot)
```

## Работа с пропущенными данными

### Поиск пропусков

```python
print(df.isnull().sum())
```

### Заполнение пропусков

```python
df['Инфляция (%)'].fillna(df['Инфляция (%)'].mean(), inplace=True)
```
