# Практический разбор по теме 7

## Наблюдение системных вызовов (strace)

### Команда

```bash
strace -c ls
```

### Что происходит

Команда `ls`:

* открывает директорию → `open()`
* читает содержимое → `read()`
* выводит результат → `write()`

### Объяснение

Программа `ls` не «читает диск».
Она обращается к ядру, которое уже работает с файловой системой и устройством.

### Связь с практикой

* любой CLI-инструмент работает через системные вызовы
* backend-приложение работает точно так же
* Python/Java внутри используют те же вызовы

## Работа с файлами

### Пример

```c
#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>

int main() {
    int fd = open("log.txt", O_CREAT | O_WRONLY | O_APPEND, 0644);

    if (fd == -1) {
        perror("open");
        return 1;
    }

    const char *msg = "User logged in\n";

    write(fd, msg, 15);

    close(fd);

    return 0;
}
```

### Компиляция

```bash
gcc file_write.c -o file_write
./file_write
```

### Что происходит

1. `open()` – ядро открывает файл и возвращает дескриптор
2. `write()` – данные передаются ядру
3. `close()` – освобождение ресурса

### Ключевой момент

Файл – это не просто объект. Это ресурс, управляемый ядром.

### Связь с практикой

Этот код – упрощённая версия:

* логирования в backend
* записи в файл
* audit-систем

Любой лог:

> logger.info() → внутри → write()

## Процессы: fork и exec

### Пример

```c
#include <unistd.h>
#include <stdio.h>
#include <sys/wait.h>

int main() {
    pid_t pid = fork();

    if (pid == -1) {
        perror("fork");
        return 1;
    }

    if (pid == 0) {
        execl("/bin/ls", "ls", "-l", NULL);
        perror("execl");
        return 1;
    } else {
        wait(NULL);
        printf("Child finished\n");
    }

    return 0;
}
```

### Что происходит

* `fork()` создаёт копию процесса
* `exec()` заменяет программу
* `wait()` ожидает завершения

### Ключевой момент

Процесс не «запускается напрямую».
Он:

1. создаётся
2. заменяется программой

### Связь с практикой

Это используется в:

* запуске серверов
* worker-процессах
* системах типа nginx, gunicorn

Любой процесс в Linux создаётся через fork + exec.

## Работа с памятью

### Пример (mmap)

```c
#include <fcntl.h>
#include <sys/mman.h>
#include <unistd.h>
#include <stdio.h>

int main() {
    int fd = open("log.txt", O_RDONLY);

    if (fd == -1) {
        perror("open");
        return 1;
    }

    char *data = mmap(NULL, 100, PROT_READ, MAP_PRIVATE, fd, 0);

    if (data == MAP_FAILED) {
        perror("mmap");
        return 1;
    }

    write(1, data, 100);

    munmap(data, 100);
    close(fd);

    return 0;
}
```

### Что происходит

* файл отображается в память
* доступ к нему как к массиву
* нет явного read()

### Ключевой момент

mmap позволяет работать с файлом как с памятью.

### Связь с практикой

Используется в:

* базах данных
* кешах
* высоконагруженных системах

## IPC (межпроцессное взаимодействие)

### Пример

```c
#include <unistd.h>
#include <stdio.h>
#include <sys/wait.h>

int main() {
    int fd[2];
    pipe(fd);

    if (fork() == 0) {
        close(fd[0]);
        write(fd[1], "Hello", 5);
        close(fd[1]);
    } else {
        close(fd[1]);
        char buffer[10] = {0};
        read(fd[0], buffer, 5);
        printf("Received: %s\n", buffer);
        close(fd[0]);
        wait(NULL);
    }

    return 0;
}
```

### Что происходит

* `pipe()` создаёт канал
* один процесс пишет
* другой читает

### Ключевой момент

Процессы не могут напрямую делиться памятью. Они взаимодействуют через ядро.

### Связь с практикой

Используется в:

* пайплайнах (Linux)
* микросервисах
* обработке данных

## Сетевые вызовы

### Пример

```c
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <netdb.h>

int main() {
    int sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock == -1) {
        perror("socket");
        return 1;
    }

    struct sockaddr_in server;
    server.sin_family = AF_INET;
    server.sin_port = htons(80);

    struct hostent *he = gethostbyname("example.com");
    if (he == NULL) {
        perror("gethostbyname");
        return 1;
    }

    memcpy(&server.sin_addr, he->h_addr_list[0], he->h_length);

    if (connect(sock, (struct sockaddr *)&server, sizeof(server)) == -1) {
        perror("connect");
        return 1;
    }

    char *request = "GET / HTTP/1.0\r\nHost: example.com\r\n\r\n";

    if (send(sock, request, strlen(request), 0) == -1) {
        perror("send");
        return 1;
    }

    char buffer[1024];
    int bytes;

    while ((bytes = recv(sock, buffer, sizeof(buffer), 0)) > 0) {
        write(1, buffer, bytes);
    }

    close(sock);
    return 0;
}
```

### Что происходит

* `socket()` – создаёт соединение
* `connect()` – подключается
* `send()` – отправляет данные
* `recv()` – получает

### Ключевой момент

Сеть – это тоже системные вызовы.

### Связь с практикой

Это:

* REST API
* HTTP
* базы данных
* любой backend

## Ошибки

### Пример

```c
#include <fcntl.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

int main() {
    int fd = open("/root/secret.txt", O_RDONLY);

    if (fd == -1) {
        printf("Error: %s\n", strerror(errno));
        return 1;
    }

    return 0;
}
```

### Что происходит

* ядро проверяет права
* при ошибке возвращает код

### Связь с практикой

Это:

* ошибки доступа
* безопасность
* HTTP 403/500

## Производительность

### Плохой вариант

```c
#include <unistd.h>

int main() {
    for (int i = 0; i < 1000; i++) {
        write(1, "a", 1);
    }
    return 0;
}
```

### Хороший вариант

```c
#include <unistd.h>

int main() {
    char buffer[1000];

    for (int i = 0; i < 1000; i++) {
        buffer[i] = 'a';
    }

    write(1, buffer, 1000);
    return 0;
}
```

### Объяснение

Каждый `write()`:

* переход в ядро
* накладные расходы

### Связь с практикой

Это:

* буферизация
* batching
* оптимизация backend
