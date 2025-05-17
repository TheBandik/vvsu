# Дополнительные структуры данных

## Stack (Стек)

Стек - это линейная структура данных, работающая по принципу LIFO (Last In, First Out), где последний добавленный элемент извлекается первым. 

**Основные операции стека:**

- `push`: добавление элемента в стек.
- `pop`: удаление верхнего элемента.
- `peek` или `top`: просмотр верхнего элемента.
- Проверка на пустоту: `is_empty`.

Стек может быть реализован на основе массива или связного списка.

**Ограничения:**

- Для реализации на массиве важно учитывать фиксированный размер.
- Для реализации на связном списке потребуется дополнительная память на хранение ссылок.

### Реализация

Простой и быстрый вариант, но требует фиксированного размера:

```python
class StackArray:
    def __init__(self, capacity):
        self.stack = [None] * capacity
        self.top = -1
        self.capacity = capacity

    def push(self, item):
        if self.top == self.capacity - 1:
            raise OverflowError("Стек переполнен")
        self.top += 1
        self.stack[self.top] = item

    def pop(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        item = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self.stack[self.top]

    def is_empty(self):
        return self.top == -1
```

### Пример

#### Задача

Дана строка, состоящая только из символов `'('`, `')'`, `'{'`, `'}'`, `'['` и `']'`. Необходимо определить, является ли заданная скобочная последовательность правильной.

Правильную скобочную последовательность можно определить следующим образом:

- пустая строка - правильная скобочная последовательность;
- правильная скобочная последовательность, взятая в скобки одного типа - правильная скобочная последовательность;
- правильная скобочная последовательность, к которой приписана слева или справа правильная скобочная последовательность - тоже правильная скобочная последовательность.

#### Решение

```python
s = input()
stack = []
for l in s:
    if len(stack) != 0:
        l1 = stack[-1] == '(' and l == ')'
        l2 = stack[-1] == '{' and l == '}'
        l3 = stack[-1] == '[' and l == ']'
        if l1 or l2 or l3:
            stack.pop()
        else:
            stack.append(l)
    else:
        stack.append(l)
if len(stack) == 0:
    print('YES')
else:
    print('NO')
```

## Queue (Очередь)

Очередь - это линейная структура данных, работающая по принципу FIFO (First In, First Out).

**Основные операции стека:** 

- `enqueue`: добавление элемента в конец очереди.
- `dequeue`: удаление элемента из начала очереди.
- `peek`: просмотр первого элемента.
- Проверка на пустоту: `is_empty`.

### Реализация

```python
class QueueArray:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0
        self.capacity = capacity

    def enqueue(self, item):
        if self.size == self.capacity:
            raise OverflowError("Очередь переполнена")
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self.queue[self.front]

    def is_empty(self):
        return self.size == 0
```

### Пример

#### Задача

В парикмахерской работает один мастер. Он тратит на одного клиента ровно 20 минут, а затем сразу переходит к следующему, если в очереди кто-то есть, либо ожидает, когда придет следующий клиент.

Даны времена прихода клиентов в парикмахерскую (в том порядке, в котором они приходили).

Также у каждого клиента есть характеристика, называемая степенью нетерпения. Она показывает, сколько человек может максимально находиться в очереди перед клиентом, чтобы он дождался своей очереди и не ушел раньше. Если в момент прихода клиента в очереди находится больше людей, чем степень его нетерпения, то он решает не ждать своей очереди и уходит. Клиент, который обслуживается в данный момент, также считается находящимся в очереди.

Требуется для каждого клиента указать время его выхода из парикмахерской.

В первой строке вводится натуральное число `N`, не превышающее `100` - количество клиентов. В следующих `N` строках вводятся времена прихода клиентов - по два числа, обозначающие часы и минуты (часы - от `0` до `23`, минуты - от `0` до `59`) и степень его нетерпения (неотрицательное целое число не большее `100`) - максимальное количество человек, которое он готов ждать впереди себя в очереди. Времена указаны в порядке возрастания (все времена различны).

Гарантируется, что всех клиентов успеют обслужить до полуночи.

Если для каких-то клиентов время окончания обслуживания одного клиента и время прихода другого совпадают, то можно считать, что в начале заканчивается обслуживание первого клиента, а потом приходит второй клиент.

Выведите `N` пар чисел: времена выхода из парикмахерской `1-го, 2-го, ... , N-гo` клиента (часы и минуты). Если на момент прихода клиента человек в очереди больше, чем степень его нетерпения, то можно считать, что время его ухода равно времени прихода.

#### Решение

```python
def calculate_exit_times(n, clients):
    def time_to_minutes(hours, minutes):
        return hours * 60 + minutes

    def minutes_to_time(minutes):
        return divmod(minutes, 60)

    queue = deque()  # Хранит время завершения обслуживания клиентов
    results = []     # Результаты времени выхода из парикмахерской для каждого клиента

    for arrival_hour, arrival_minute, impatience in clients:
        arrival_time = time_to_minutes(arrival_hour, arrival_minute)

        # Удаляем из очереди всех, чье обслуживание завершилось до прихода текущего клиента
        while queue and queue[0] <= arrival_time:
            queue.popleft()

        # Проверяем, может ли клиент остаться
        if len(queue) > impatience:
            # Клиент уходит, так как очередь слишком большая
            results.append((arrival_hour, arrival_minute))  # Время ухода = время прихода
        else:
            # Клиент остается, добавляем его в очередь
            if queue:
                start_service_time = max(queue[-1], arrival_time)
            else:
                start_service_time = arrival_time

            end_service_time = start_service_time + 20  # 20 минут на обслуживание
            queue.append(end_service_time)
            results.append(minutes_to_time(end_service_time))
    
    return results

n = int(input())
clients = []
for _ in range(n):
    h, m, impatience = [int(x) for x in input().split()]
    clients.append((h, m, impatience))

exit_times = calculate_exit_times(n, clients)

for hours, minutes in exit_times:
    print(hours, minutes)
```
