# Основы HTML и CSS для работы с API

## Введение

HTML (HyperText Markup Language) и CSS (Cascading Style Sheets) являются основными технологиями для создания веб-страниц. HTML определяет структуру страницы, а CSS отвечает за её внешний вид. При работе с API (Application Programming Interface) HTML и CSS используются для отображения данных, полученных из внешних источников.

## 1. Основы HTML

### 1.1 Структура HTML-документа

Каждый HTML-документ имеет стандартную структуру:
```html
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Простая страница</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Добро пожаловать!</h1>
    <p>Это простая HTML-страница.</p>
</body>
</html>
```

- `<!DOCTYPE html>` – объявляет документ HTML5.
- `<head>` – содержит метаданные и ссылки на внешние ресурсы.
- `<body>` – основное содержимое страницы.
- `<form>` – форма для добавления задач напрямую в FastAPI.
- `<iframe>` – отображает список задач, полученных из API.

### 1.2 Основные HTML-теги

- `<div>` – контейнер для группировки элементов.
- `<h1> - <h6>` – заголовки разного уровня.
- `<p>` – абзац текста.
- `<button>` – кнопка для взаимодействия с пользователем.
- `<input>` – поле ввода.

## 2. Основы CSS

### 2.1 Подключение CSS

CSS можно подключить тремя способами:

1. Внешний файл:

```html
<link rel="stylesheet" href="styles.css">
```
2. Встроенный стиль в `<head>`:
   
```html
<style>
    body { background-color: #f4f4f4; }
</style>
```

3. Внутренние стили в атрибуте `style`:

```html
<div style="color: red;">Текст</div>
```

### 2.2 Основные CSS-свойства

- `color` – цвет текста.
- `background-color` – цвет фона.
- `font-size` – размер шрифта.
- `margin` – внешний отступ.
- `padding` – внутренний отступ.
- `display` – тип отображения (`block`, `inline`, `flex`).

Пример файла `styles.css`:
```css
body {
    font-family: Arial, sans-serif;
    background-color: #f9f9f9;
    text-align: center;
}

button {
    padding: 10px 20px;
    background-color: blue;
    color: white;
    border: none;
    cursor: pointer;
}

form {
    margin-bottom: 20px;
}

iframe {
    border: none;
}
```

## 3. Фронтенд для FastAPI

Теперь создадим интерфейс для взаимодействия с FastAPI-сервером.

### 3.1 HTML для отображения задач

```html
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Task Manager</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Список задач</h1>
    <form action="http://127.0.0.1:8000/tasks" method="post">
        <input type="text" name="title" placeholder="Введите задачу" required>
        <button type="submit">Добавить</button>
    </form>
    <iframe src="http://127.0.0.1:8000/tasks" width="100%" height="400px"></iframe>
</body>
</html>
```

### 3.2 Как это работает

- Форма отправляет данные в FastAPI с помощью метода `POST`.
- `iframe` отображает список задач, полученных по `GET`-запросу.
- Пользователь может взаимодействовать с API без JavaScript, только через HTML и CSS.

Таким образом, мы создали полноценный интерфейс для взаимодействия с FastAPI напрямую через HTML.
