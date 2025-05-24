# Лабораторная работа №6

Для написания регулярных выражений лучше всего использовать помогающие сервисы, такие как https://regex101.com/

## Задание №1

1. Изучить лог-файл и определить типы сообщений
2. Создать регулярные выражения для определения даты и времени, типа ошибки, имени пользователя, IP-адреса, доступное место на диске и температуру процессора
3. Написать на языке программирования программу, которая соберет нужную информацию по регулярным выражениям
4. Реализовать алгоритм, который будет определять наличие проблемы в виде высокой температуры процессора и выводит соответствующее сообщение в консоль вместе с датой и временем.

### Лог

```
2023-03-24 12:30:00 INFO: User login successful. User: john.doe, IP address: 192.168.0.1
2023-03-24 12:31:00 ERROR: Database connection failed. Error code: 12345
2023-03-24 12:32:00 WARNING: Disk space is low. Available space: 10GB
2023-03-24 12:33:00 DEBUG: Sent email to john.doe@example.com with subject "New features".
2023-03-24 12:34:00 INFO: User logout successful. User: john.doe, IP address: 192.168.0.1
2023-03-24 12:35:00 WARNING: CPU temperature is high. Temperature: 80C
2023-03-24 12:36:00 INFO: User login successful. User: jane.doe, IP address: 192.168.0.2
2023-03-24 12:37:00 DEBUG: Processing request from IP address: 192.168.0.2, URL: /dashboard
2023-03-24 12:38:00 INFO: User logout successful. User: jane.doe, IP address: 192.168.0.2
2023-03-24 12:39:00 ERROR: File not found. File path: /var/www/html/index.html
2023-03-24 12:40:00 WARNING: Server load is high. Load average: 4.5
2023-03-24 12:41:00 DEBUG: Sent email to jane.doe@example.com with subject "System update".
2023-03-24 12:42:00 INFO: User login successful. User: johndoe, IP address: 192.168.0.3
2023-03-24 12:43:00 ERROR: Invalid credentials. User: johndoe
2023-03-24 12:44:00 WARNING: Disk space is low. Available space: 5GB
2023-03-24 12:45:00 DEBUG: Processing request from IP address: 192.168.0.3, URL: /admin
2023-03-24 12:46:00 INFO: User logout successful. User: johndoe, IP address: 192.168.0.3
2023-03-24 12:47:00 ERROR: Database query failed. Query: SELECT * FROM users WHERE id=100
2023-03-24 12:48:00 WARNING: CPU temperature is high. Temperature: 85C
2023-03-24 12:49:00 DEBUG: Sent email to johndoe@example.com with subject "Security alert".
2023-03-24 12:50:00 INFO: User login successful. User: janedoe, IP address: 192.168.0.4
2023-03-24 12:51:00 ERROR: Internal server error. Error message: Division by zero
2023-03-24 12:52:00 WARNING: Server load is high. Load average: 5.5
2023-03-24 12:53:00 DEBUG: Processing request from IP address: 192.168.0.4, URL: /dashboard
2023-03-24 12:54:00 INFO: User logout successful. User: janedoe, IP address: 192.168.0.4
2023-03-24 12:33:00 INFO: New user registered. User: jane.doe, Email: jane.doe@email.com
2023-03-24 12:34:00 ERROR: Failed to process request. User: john.doe, Error message: "Invalid request"
2023-03-24 12:35:00 WARNING: CPU temperature is high. Temperature: 80°C
2023-03-24 12:36:00 INFO: User logout successful. User: john.doe, IP address: 192.168.0.1
2023-03-24 12:37:00 ERROR: File not found. Filename: myfile.txt
2023-03-24 12:38:00 WARNING: Server load is high. Load average: 4.5
2023-03-24 12:39:00 INFO: User login successful. User: jane.doe, IP address: 192.168.0.2
2023-03-24 12:40:00 ERROR: Unable to send email. Error message: "SMTP connection error"
2023-03-24 12:41:00 WARNING: Disk space is low. Available space: 5GB
2023-03-24 12:42:00 INFO: New user registered. User: bob.smith, Email: bob.smith@email.com
2023-03-24 12:43:00 ERROR: Database query failed. Error code: 67890
2023-03-24 12:44:00 WARNING: CPU temperature is high. Temperature: 85°C
2023-03-24 12:45:00 INFO: User logout successful. User: jane.doe, IP address: 192.168.0.2
2023-03-24 12:46:00 ERROR: Permission denied. User: bob.smith, File: myfile.txt
2023-03-24 12:47:00 WARNING: Server load is high. Load average: 5.0
2023-03-24 12:48:00 INFO: User login successful. User: john.doe, IP address: 192.168.0.1
2023-03-24 12:49:00 ERROR: Unable to connect to database. Error message: "Connection refused"
2023-03-24 12:50:00 WARNING: Disk space is low. Available space: 2GB
2023-03-24 12:51:00 INFO: User login successful. User: bob.smith, IP address: 192.168.0.3
2023-03-24 12:52:00 ERROR: Failed to process request. User: jane.doe, Error message: "Invalid request"
2023-03-24 12:53:00 WARNING: CPU temperature is high. Temperature: 90°C
2023-03-24 12:54:00 INFO: User logout successful. User: john.doe, IP address: 192.168.0.1
2023-03-24 12:55:00 ERROR: File not found. Filename: myfile2.txt
2023-03-24 12:56:00 WARNING: Server load is high. Load average: 5.5
2023-03-24 12:57:00 INFO: User login successful. User: jane.doe, IP address: 192.168.0.2
2023-03-24 12:58:00 ERROR: Failed to connect to API. Error code: 543
2023-03-24 13:00:00 INFO: User login successful. User: alice.smith, IP address: 10.20.30.40
2023-03-24 13:01:00 ERROR: Unable to send email. Error code: 67890
2023-03-24 13:02:00 WARNING: CPU temperature is high. Current temperature: 80°C
2023-03-24 13:03:00 INFO: User login successful. User: bob.johnson, IP address: 192.168.1.1
2023-03-24 13:04:00 ERROR: Database connection failed. Error code: 23456
2023-03-24 13:05:00 WARNING: Disk space is low. Available space: 5GB
2023-03-24 13:06:00 INFO: User logout. User: alice.smith, IP address: 10.20.30.40
2023-03-24 13:07:00 ERROR: Unable to write to file. Error code: 34567
2023-03-24 13:08:00 WARNING: CPU usage is high. Current usage: 90%
2023-03-24 14:00:00 INFO: User login successful. User: david.lee, IP address: 192.168.0.10
2023-03-24 14:01:00 ERROR: Authentication failed. Error code: 98765
2023-03-24 14:02:00 WARNING: Memory usage is high. Current usage: 80%
2023-03-24 14:03:00 INFO: User login successful. User: emily.nguyen, IP address: 10.0.0.1
2023-03-24 14:04:00 ERROR: Database query failed. Error code: 45678
2023-03-24 14:05:00 WARNING: Disk space is low. Available space: 1GB
2023-03-24 14:06:00 INFO: User logout. User: david.lee, IP address: 192.168.0.10
2023-03-24 14:07:00 ERROR: Unable to write to file. Error code: 56789
2023-03-24 14:08:00 WARNING: CPU temperature is high. Current temperature: 85°C
2023-03-24 15:00:00 INFO: System startup. Operating system: Windows 10, Kernel version: 10.0.19042.0
2023-03-24 15:01:00 ERROR: Unable to start application. Error code: 34567
2023-03-24 15:02:00 WARNING: Disk health is poor. S.M.A.R.T status: failing
2023-03-24 15:03:00 INFO: User login successful. User: fred.smith, IP address: 192.168.1.2
2023-03-24 15:04:00 ERROR: Database connection failed. Error code: 67890
2023-03-24 15:05:00 WARNING: Disk space is low. Available space: 2GB
2023-03-24 15:06:00 INFO: User logout. User: fred.smith, IP address: 192.168.1.2
2023-03-24 15:07:00 ERROR: Unable to connect to network printer. Error code: 89012
2023-03-24 15:08:00 WARNING: Battery is low. Remaining charge: 10%
2023-03-24 18:00:00 INFO: Server start. Host: myserver.local, IP address: 192.168.0.10
2023-03-24 18:01:00 ERROR: Failed to execute command. Command: "rm -rf /", User: root
2023-03-24 18:02:00 WARNING: CPU temperature is high. Temperature: 85°C
2023-03-24 18:03:00 INFO: User login successful. User: jennifer.smith, IP address: 192.168.0.20
2023-03-24 18:04:00 ERROR: Unable to connect to VPN. Error code: 23456
2023-03-24 18:05:00 WARNING: Disk space is low. Available space: 500MB
2023-03-24 18:06:00 INFO: User logout. User: jennifer.smith, IP address: 192.168.0.20
2023-03-24 18:07:00 ERROR: Unable to access file. File: /var/log/messages, User: jennifer.smith
2023-03-24 18:08:00 WARNING: Memory usage is high. Available memory: 500MB
2023-03-24 22:00:00 INFO: Application started. Version: 1.2.3, Environment: production
2023-03-24 22:01:00 ERROR: Database connection failed. Error code: 54321
2023-03-24 22:02:00 WARNING: Disk space is low. Available space: 2GB
2023-03-24 22:03:00 INFO: User registration. User: alice.smith, Email: alice.smith@example.com
2023-03-24 22:04:00 ERROR: Unable to execute query. Query: "SELECT * FROM users", User: admin
2023-03-24 22:05:00 WARNING: CPU usage is high. Usage: 90%
2023-03-24 22:06:00 INFO: User login successful. User: bob.johnson, IP address: 192.168.1.10
2023-03-24 22:07:00 ERROR: Unable to send email. Recipient: bob.johnson@example.com, Error code: 12345
2023-03-24 22:08:00 WARNING: Memory usage is high. Available memory: 200MB
2023-03-24 22:09:00 INFO: Application stopped.
```

## Задание №2

Имеется набор строк с адресами. В каждом адресе нужно убрать лишнее. 

В таблице ниже указаны:
+ входные данные
+ выходные данные, которые должны получится после обработки regex
+ комментарий, где даётся некоторое пояснение

Нужно написать правила замены. Правила замены применяются последовательно для входных данных, в том порядке, в котором они указаны. Делается попытка применить все правила замены для каждой строки, нельзя остановиться в каком-то месте.

Результирующие адреса могут отличаться от требуемых в таблице, но незначительно. То есть если в эталоне один пробел, а получилось два - это нормально. А вот терять точки и запятые - неправильно. Можно добавлять запятые, но только в правильных местах.

В таблице приведены шаблоны ошибок. Если при изменении какой-нибудь цифры в адресе, которое подходит по шаблону, правило перестанет работать, это неправильно.

Как проверить себя:

1. Написали список правил
2. Взяли список исходных адресов
3. Применили ко всему списку правило 1
4. Применили ко всему списку правило 2
    ...
5. Применили последнее правило
6. Сверили результат с колонкой «Что надо получить», обращая внимание на комментарии. Ничего не потерялось?
7. Если потерялось / испортилось, то находим баг в регулярках, исправляем, и повторяем все шаги с самого начала

Адреса:

| Входной адрес                                        | Что надо получить                               | Комментарий                                                                                                                                                      |
| ---------------------------------------------------- | ----------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 140002 ЛЮБЕРЦЫ 2 ОКТЯБРЬСКИЙ ПР 123/4-115            | 140002 ЛЮБЕРЦЫ ОКТЯБРЬСКИЙ ПР 123/4-115         | После названия города может идти цифра, совпадающая с концом индекса. Это номер почтового отделения. Это не адресная информация, надо убрать.                    |
| 636450 636450, Г. ТОГУР, УЛ. БЕЛИНСКОГО Д. 6 КВ 2    | 636450, Г. ТОГУР, УЛ. БЕЛИНСКОГО Д. 6 КВ 2      | Дублирование индексов - не смертельно, но нехорошо. Убрать.                                                                                                      |
| 423571 423571 НИЖНЕКАМСК 1 ТАТАРСТАН ВАХИТОВА 51-171 | 423571 НИЖНЕКАМСК ТАТАРСТАН ВАХИТОВА 51-171     | Комбинация первых двух случаев.                                                                                                                                  |
| 658219 РУБЦОВСК 19 УЛ. ЖЕЛЕЗНОДОРОЖНАЯ 194           | 658219 РУБЦОВСК УЛ. ЖЕЛЕЗНОДОРОЖНАЯ 194         | Номер отделения может состоять из двух цифр.                                                                                                                     |
| 622049 НИЖНИЙ ТАГИЛ 49 УРАЛЬСКИЙ ПР 54-252           | 622049 НИЖНИЙ ТАГИЛ УРАЛЬСКИЙ ПР 54-252         | Город - не обязательно одно слово.                                                                                                                               |
| 127543 МОСКВА 543,МОСКВА 543,КОНЕНКОВА 12-32         | 127543 МОСКВА,КОНЕНКОВА 12-32                   | Часть с номером отделения может повторяться.                                                                                                                     |
| 391112 РЫБНОВСКИЙ РАЙОН, РЫБНОЕ 2 БОЛЬШАЯ 18-33      | 391112 РЫБНОВСКИЙ РАЙОН, РЫБНОЕ БОЛЬШАЯ 18-33   | Может и район быть.                                                                                                                                              |
| 622049 НИЖНИЙ ТАГИЛ, УРАЛЬСКИЙ ПР 49 252             | 622049 НИЖНИЙ ТАГИЛ, УРАЛЬСКИЙ ПР 49 252        | А тут 49 - номер дома, терять нельзя                                                                                                                             |
| 644103 ОМСК 103 3 МАТЕРИАЛЬНЫЙ ПЕР 45                | 644103 ОМСК 3 МАТЕРИАЛЬНЫЙ ПЕР 45               | Нельзя потерять 3, она относится к улице                                                                                                                         |
| 431451 РУЗАЕВКА 11 ШКОЛЬНЫЙ БУЛЬВАР Д 2 Б КВ 27      | 431451 РУЗАЕВКА ШКОЛЬНЫЙ БУЛЬВАР Д 2 Б КВ 27    | Есть и хитрые номера отделений, они состоят из двух цифр (всегда), причём последняя совпадает с последней цифрой индекса, а первая с предпоследней не совпадает. |
