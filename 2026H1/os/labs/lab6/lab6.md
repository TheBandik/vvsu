# Лабораторная работа №6

Форма сдачи лабораторной работы:
- исходный код утилиты;
- демонстрация работы утилиты.

## Цель работы

Необходимо разработать консольную утилиту для анализа файловой системы, позволяющую:
* исследовать структуру каталогов;
* анализировать использование дискового пространства;
* выявлять дубликаты файлов;
* обнаруживать особенности хранения данных (ссылки, различие размеров).

## Требования к программе

Реализовать CLI-утилиту:

```bash
fs-inspector <path> [options]
```

где:

* `<path>` – анализируемый каталог;
* `[options]` – режим работы.

## Поддерживаемые режимы

### Общая статистика

```bash
fs-inspector <path> --summary
```

Вывести:

* количество файлов;
* количество каталогов;
* суммарный логический размер.

### Реальный размер

```bash
fs-inspector <path> --real-size
```

Дополнительно вывести:

* фактический размер (с учётом блоков файловой системы)


### Крупнейшие файлы

```bash
fs-inspector <path> --top N
```

Вывести N самых больших файлов.


### Дубликаты

```bash
fs-inspector <path> --duplicates
```

Найти файлы с одинаковым содержимым.


### Жёсткие ссылки

```bash
fs-inspector <path> --links
```

Найти файлы, указывающие на один и тот же объект файловой системы.


### Символические ссылки

```bash
fs-inspector <path> --symlinks
```

Вывести:

* путь ссылки;
* целевой путь;
* статус (OK / BROKEN).


## Требования к реализации

### Обход файловой системы

* рекурсивный обход;
* корректная работа с вложенными каталогами;
* защита от зацикливания (symlink).

### Модель файла

Для каждого файла учитывать:

* путь;
* размер;
* inode / file identifier;
* количество блоков (если доступно);
* тип (файл, каталог, ссылка).

### Подсчёт размера

#### Логический размер

* сумма размеров файлов.

#### Реальный размер

* учитывать `st_blocks` (или аналог).

### Жёсткие ссылки

> Один inode должен учитываться только один раз.

### Дубликаты

Алгоритм:

1. группировка по размеру;
2. вычисление hash (например, SHA-256);
3. сравнение.

### Символические ссылки

* определять ссылку;
* получать целевой путь;
* проверять существование.

## Ограничения

* без sudo;
* без вызова внешних утилит (`du`, `ls`, `find` и др.);
* только стандартные библиотеки.


## Тестовый набор (обязательный)

Создать структуру:

```bash
mkdir -p lab_fs/docs lab_fs/images lab_fs/links lab_fs/sparse

echo "Hello FS" > lab_fs/docs/report.txt
cp lab_fs/docs/report.txt lab_fs/docs/report_copy.txt
touch lab_fs/docs/empty.txt

dd if=/dev/urandom of=lab_fs/images/img1.bin bs=1K count=10
cp lab_fs/images/img1.bin lab_fs/images/img2.bin

ln lab_fs/docs/report.txt lab_fs/links/hardlink_to_report

ln -s ../docs/report.txt lab_fs/links/symlink_to_report
ln -s ../docs/missing.txt lab_fs/links/broken_link

dd if=/dev/zero of=lab_fs/sparse/sparse.bin bs=1 count=0 seek=100M
```

## Ожидаемые результаты

### Summary

```bash
fs-inspector lab_fs --summary
```

* корректное количество файлов и директорий;
* размер учитывает все файлы.

### Real size

```bash
fs-inspector lab_fs --real-size
```

* логический размер ≫ реального (из-за sparse).

### Duplicates

```bash
fs-inspector lab_fs --duplicates
```

* `report.txt` = `report_copy.txt`;
* `img1.bin` = `img2.bin`.

### Links

```bash
fs-inspector lab_fs --links
```

* `report.txt` и `hardlink_to_report` имеют один inode.

### Symlinks

```bash
fs-inspector lab_fs --symlinks
```

* одна валидная ссылка;
* одна битая.

### Top

```bash
fs-inspector lab_fs --top 3
```

* sparse файл должен быть в топе.
