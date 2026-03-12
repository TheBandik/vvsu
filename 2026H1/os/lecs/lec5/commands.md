# Практический разбор по теме 5

## Cron и запуск процессов по расписанию

# 1. Проверяем наличие cron

## Найти процесс cron

```
ps aux | grep cron
```

или

```
ps aux | grep crond
```

## Проверяем службу

### Linux (systemd)

```
systemctl status cron
```

или

```
systemctl status crond
```

### macOS

```
launchctl list | grep cron
```

# 2. Где хранятся задачи cron

## Пользовательские задачи

```
crontab -l
```

Если задач нет:

```
no crontab for user
```

## Редактирование таблицы

```
crontab -e
```

Это открывает **личную таблицу заданий пользователя**.

# 3. Системные задания cron

Посмотреть системные каталоги:

```
ls /etc/cron.*
```

Обычно можно увидеть:

```
cron.hourly
cron.daily
cron.weekly
cron.monthly
```

### macOS

Подобные файлы отсутствуют.

## Посмотреть содержимое

```
ls /etc/cron.daily
```

Можно показать реальные задачи системы:

```
logrotate
apt
man-db
```

# 4. Создаём свою cron-задачу

## Открываем таблицу

```
crontab -e
```

Добавляем строку:

```
* * * * * date >> ~/cron_demo.txt
```

Сохранить файл.

# 5. Наблюдаем выполнение

Подождать 1–2 минуты.

Проверить файл:

```
cat ~/cron_demo.txt
```

Результат:

```
Thu Mar 12 12:01:00
Thu Mar 12 12:02:00
```

cron **каждую минуту запускает команду**.

# 6. Наблюдаем запуск процесса

Открыть второй терминал:

```
watch -n 1 "ps aux | grep date"
```

Когда cron запускает задачу – можно увидеть **кратковременный процесс**.

### macOS

Подобная команда отсутствует.

# 7. Запускаем более долгую задачу

Изменим cron.

```
crontab -e
```

Добавим:

```
* * * * * sleep 30
```

Теперь задача выполняется **30 секунд**.

## Наблюдаем процесс

```
ps aux | grep sleep
```

Можно увидеть:

```
sleep 30
```

# 8. Проверяем родителя процесса

Запустить долгую задачу:

```
* * * * * sleep 40
```

Найти процесс:

### Linux

```
ps -o pid,ppid,cmd | grep sleep
```

### macOS

```
ps -o pid,ppid,command | grep sleep
```

Родителем процесса будет **cron**.

# 9. Проверяем лог cron

### Linux

```
journalctl -u cron
```

или

```
grep CRON /var/log/syslog
```

Можно увидеть записи:

```
CRON[1234]: (user) CMD (date >> cron_demo.txt)
```

### macOS

cron пишет в системный лог:

```
grep cron /var/log/system.log
```

или

```
log show --predicate 'process == "cron"' --last 10m
```

# 10. Нагрузка cron

Добавим несколько задач:

```
* * * * * sleep 50
* * * * * sleep 50
* * * * * sleep 50
```

Проверим:

```
ps aux | grep sleep
```

# 11. Остановка заданий

Открыть:

```
crontab -e
```

Удалить строки.

Проверить:

```
crontab -l
```
