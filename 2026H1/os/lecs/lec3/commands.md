# Практический разбор по теме 3

## Процесс как объект ядра

### Создаём процесс

```
sleep 1000 &
echo $!
```

### Смотрим состояние

#### Linux

```
ps -o pid,ppid,state,cmd -p <PID>
```

#### macOS

```
ps -o pid,ppid,state,command -p <PID>
```

### Структура процесса

#### Linux

```
# Структура процесса
cat /proc/<PID>/status

# Память процесса
cat /proc/<PID>/maps | head

# Файловые дескрипторы
ls -l /proc/<PID>/fd
```

#### macOS

```
# Структура процесса
ps -o pid,ppid,state,%mem,command -p <PID>

# Память процесса
vmmap <PID>

# Файловые дескрипторы
lsof -p <PID>
```

## Родитель, потомок, усыновление

### Определяем себя

```
echo $$
echo $PPID
```

### Создаём вложенную оболочку

```
bash
sleep 1000 &
```

#### Linux

```
ps -o pid,ppid,cmd
```

#### macOS

```
ps -o pid,ppid,command
```

### Усыновление (orphan)

Внутри вложенной оболочки:

```
sleep 300 &
exit
```

В основной оболочке:

#### Linux

```
ps -o pid,ppid,cmd
```

#### macOS

```
ps -o pid,ppid,command
```

## Zombie

### Создание zombie

```
bash -c 'sleep 1 & exit'
ps -el | grep Z
```

## Связь с загрузкой

#### Linux

```
ps -p 1 -o pid,cmd
```

#### macOS

```
ps -p 1 -o pid,command
```