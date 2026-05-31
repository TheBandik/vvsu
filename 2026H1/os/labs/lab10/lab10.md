# Лабораторная работа №10

---

Форма сдачи лабораторной работы:

- исходный код приложения, `Dockerfile`, `docker-compose.yaml`, `.dockerignore`;
- README с командами и кратким описанием того, что произошло на каждом шаге;
- скриншоты ключевых моментов выполнения.

## Справка

---

### Что мы делаем

В прошлой лабораторной мы поднимали **готовые** образы из Docker Hub. Теперь мы:

1. **Соберём свой образ** из исходного кода – напишем приложение, опишем его сборку в `Dockerfile`, получим запускаемый образ.
2. **Объединим несколько контейнеров** в один стек: само приложение + база данных. Опишем стек в `docker-compose.yaml` и запустим всё одной командой.

### Что такое Dockerfile

> **Dockerfile** – текстовый файл-рецепт сборки образа. Каждая строка – одна инструкция, каждая инструкция (как правило) создаёт один слой.

Минимальный пример:

```dockerfile
FROM python:3.12-alpine               # с какого базового образа стартуем
WORKDIR /app                          # рабочая директория внутри образа
COPY requirements.txt .               # копируем файл из текущей папки в /app
RUN pip install -r requirements.txt   # выполняем команду при сборке
COPY . .                              # копируем остальной код
CMD ["python3", "main.py"]             # команда, которая запустится при docker run
```

Сборка образа из такого Dockerfile:

```bash
docker build -t myapp:1.0 .
```

`-t myapp:1.0` – имя и тег образа. `.` – папка, где лежит Dockerfile.

### Что такое docker-compose

> **docker-compose** – инструмент, описывающий несколько связанных контейнеров в одном YAML-файле. Поднимает весь стек одной командой `docker compose up`.

Минимальный пример `docker-compose.yaml`:

```yaml
services:
  web:
    build: .
    ports:
      - "8080:5000"
  db:
    image: postgres:16
    environment:
      POSTGRES_PASSWORD: secret
```

Внутри compose-сети сервисы видят друг друга по имени: `web` достучится до БД по адресу `db:5432`. Никакой ручной настройки сети не требуется – Docker сделает её сам.

### Тома

Контейнер – временная сущность. Удалили – пропали данные. Чтобы данные пережили перезапуск, нужны **тома** (volumes). Том – это управляемое Docker хранилище на хосте, которое подключается в контейнер.

```yaml
services:
  db:
    image: postgres:16
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```

Том `pgdata` создаётся автоматически, монтируется в `/var/lib/postgresql/data` контейнера. Удалили контейнер – том остался. Создали новый контейнер с тем же томом – данные на месте.

---

## Задание 1. Собрать свой образ

Цель – научиться писать `Dockerfile` и собирать собственный образ.

### Что собираем

Мини веб-приложение **«Счётчик посещений»**: при заходе в браузер на `/` показывает, какой по счёту вы посетитель. Пока без БД – счётчик хранится в памяти процесса.

### Шаг 1. Создать папку проекта

```
counter/
├── main.py
└── requirements.txt
```

Содержимое `requirements.txt`:

```
flask==3.0.0
```

Содержимое `main.py` (на Python с Flask – самый короткий вариант):

```python
import os
from flask import Flask

app = Flask(__name__)
counter = 0

@app.route("/")
def index():
    global counter
    counter += 1
    host = os.uname().nodename
    return f"<h1>Привет! Вы посетитель №{counter}</h1><p>Хост: {host}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

> **Не хотите Python?** Можно сделать на любом языке. Например, Node.js (Express): `app.get('/', (req, res) => res.send('Hello'))`. Главное – чтобы приложение слушало HTTP на каком-то порту и отвечало текстом. Логика – на ваше усмотрение, лишь бы было что показать в браузере.

### Шаг 2. Написать Dockerfile

Создайте файл `Dockerfile` в той же папке:

```dockerfile
FROM python:3.12-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "main.py"]
```

### Шаг 3. Создать .dockerignore

Чтобы в образ не попадало лишнее, рядом с `Dockerfile` положите `.dockerignore`:

```
.git
__pycache__
*.pyc
.venv
.env
*.log
.idea
.vscode
```

### Шаг 4. Собрать образ

```bash
docker build -t counter:1.0 .
```

Посмотрите вывод – Docker печатает каждый шаг сборки и кэширование слоёв.

Проверьте, что образ появился:

```bash
docker images | grep counter
```

### Шаг 5. Запустить контейнер

```bash
docker run -d --name counter -p 8080:5000 counter:1.0
```

Откройте `http://localhost:8080` в браузере. Обновите страницу несколько раз – счётчик должен расти.

### Шаг 6. Проверить кэш слоёв

Это важная часть про то, **зачем** нужен правильный порядок инструкций в Dockerfile.

1. Соберите образ ещё раз: `docker build -t counter:1.0 .` – все слои берутся из кэша мгновенно.
2. Откройте `main.py`, измените сообщение (например, добавьте смайлик в строку с приветствием).
3. Соберите снова: `docker build -t counter:1.0 .`. Слой `RUN pip install ...` **не пересобирается** (использует кэш), пересобирается только `COPY . .` и финальные слои.
4. Откройте `requirements.txt`, добавьте новую строку (например, `requests==2.31.0`).
5. Соберите снова. Теперь `pip install` **пересобирается** – зависимости поменялись.

### Шаг 7. Очистка

```bash
docker rm -f counter
```

(образ оставьте – он пригодится в задании 2)

---

## Задание 2. Собрать стек через docker-compose

Цель – связать приложение с базой данных через `docker-compose.yaml`. Счётчик теперь должен храниться в **PostgreSQL**, а не в памяти процесса.

### Шаг 1. Доработать приложение

Добавьте в `requirements.txt`:

```
flask==3.0.0
psycopg2-binary==2.9.9
```

Перепишите `main.py` так, чтобы счётчик хранился в БД:

```python
import os
import psycopg2
from flask import Flask

app = Flask(__name__)

def connect():
    return psycopg2.connect(os.environ["DATABASE_URL"])

def init_db():
    with connect() as conn, conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS visits (
                id SERIAL PRIMARY KEY,
                ts TIMESTAMP DEFAULT NOW()
            )
        """)

@app.route("/")
def index():
    with connect() as conn, conn.cursor() as cur:
        cur.execute("INSERT INTO visits DEFAULT VALUES")
        cur.execute("SELECT COUNT(*) FROM visits")
        count = cur.fetchone()[0]
    host = os.uname().nodename
    return f"<h1>Привет! Вы посетитель №{count}</h1><p>Хост: {host}</p>"

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
```

Адрес БД приложение берёт из переменной окружения `DATABASE_URL`. Мы её зададим в compose.

### Шаг 2. Написать docker-compose.yaml

Рядом с `Dockerfile` создайте файл `docker-compose.yaml`:

```yaml
services:
  db:
    image: postgres:16
    environment:
      POSTGRES_USER: counter
      POSTGRES_PASSWORD: secret
      POSTGRES_DB: counter
    volumes:
      - pgdata:/var/lib/postgresql/data
    restart: unless-stopped

  web:
    build: .
    ports:
      - "8080:5000"
    environment:
      DATABASE_URL: postgresql://counter:secret@db:5432/counter
    depends_on:
      - db
    restart: unless-stopped

volumes:
  pgdata:
```

### Шаг 3. Поднять стек

```bash
docker compose up -d --build
```

`--build` – пересобрать образ `web` перед запуском (нужно при первом запуске и после изменений в коде).

Откройте `http://localhost:8080`. Обновите несколько раз. Должен расти счётчик.

### Шаг 4. Посмотреть статус и логи

```bash
docker compose ps           # статус сервисов
docker compose logs         # все логи
docker compose logs -f web  # логи web в реальном времени
```

В логах БД при первом старте видно создание базы и пользователя. В логах `web` – запросы Flask.

### Шаг 5. Проверить персистентность тома

Самая важная проверка – переживут ли данные пересоздание контейнера.

1. Сделайте несколько посещений, запомните последнее число (например, 10).
2. Остановите и удалите контейнеры (но **не тома**):
   ```bash
   docker compose down
   ```
3. Снова поднимите стек:
   ```bash
   docker compose up -d
   ```
4. Откройте сайт. Счётчик должен продолжиться с 11, а не с 1 – данные сохранились в томе.

### Шаг 6. Заглянуть внутрь БД

```bash
docker compose exec db psql -U counter -d counter
```

Внутри psql:

```sql
SELECT COUNT(*) FROM visits;
SELECT * FROM visits ORDER BY ts DESC LIMIT 5;
\q
```

Сделайте скриншот – должно быть видно записи в таблице.

### Шаг 7. Уборка

```bash
docker compose down          # остановить и удалить контейнеры, том остаётся
# или
docker compose down -v       # + удалить том (данные пропадут!)
```

---

## Дополнительные задания

### A. Multi-stage build для Python

Сейчас в образе остаются файлы `requirements.txt` и `__pycache__`, а также служебные данные от pip. Перепишите `Dockerfile` в multi-stage стиле: на первой стадии установите зависимости в отдельную папку, на второй – соберите финальный образ только с кодом и установленными библиотеками.

Посмотрите размер «до» и «после»:

```bash
docker images counter
```

### B. Nginx как reverse-proxy

Добавьте в compose третий сервис – `nginx`, который слушает порт 80 и проксирует запросы в `web:5000`. Уберите проброс порта у `web` – пусть он будет доступен только внутри compose-сети.

Подсказка: используйте образ `nginx:alpine`, конфигурацию монтируйте через volume.

### C. Healthcheck

Добавьте healthcheck в compose: web должен дождаться, пока БД будет готова, прежде чем стартовать. Это решает проблему гонки запуска – сейчас при первом старте `web` может попытаться подключиться к БД до того, как postgres готов принимать соединения.

Подсказка:

```yaml
db:
  healthcheck:
    test: ["CMD-SHELL", "pg_isready -U counter"]
    interval: 5s
    timeout: 3s
    retries: 5

web:
  depends_on:
    db:
      condition: service_healthy
```

### D. Лимиты ресурсов

Добавьте `deploy.resources.limits` для `web` (например, 256 MB памяти и 0.5 CPU). Посмотрите `docker stats` – значения в колонке `MEM USAGE / LIMIT` должны совпадать с заданным лимитом.

### E. Своя «фишка»

Сделайте приложение чуть более интересным: добавьте страницу со списком последних 10 посещений (с датой), форму ввода имени, любую другую идею.
