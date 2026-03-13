# Лабораторная работа №2

Для предложенного по варианту (номер в таблице успеваемости) алгоритма необходимо:
- построить блок-схему алгоритма;
- определить временную сложность алгоритма.

---

# Вариант 1

```python
arr = [5, 2, 9, 1, 7]

count = 0

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i] > arr[j]:
            count += 1

result = count
```

---

# Вариант 2

```python
arr = [5, 2, 9, 1, 7]

max_val = arr[0]

for x in arr:
    if x > max_val:
        max_val = x

result = max_val
```

---

# Вариант 3

```python
arr = [5, 2, 9, 1, 7]

count = 0

for i in range(len(arr)):
    for j in range(len(arr)):
        if (arr[i] + arr[j]) % 2 == 0:
            count += 1

result = count
```

---

# Вариант 4

```python
arr = [5, 2, 9, 1, 7]

sum_triplets = 0

for i in range(len(arr)):
    for j in range(len(arr)):
        for k in range(len(arr)):
            sum_triplets += arr[i] + arr[j] + arr[k]

result = sum_triplets
```

---

# Вариант 5

```python
arr = [5, 2, 9, 1, 7]

total = 0

for x in arr:
    total += x

result = total
```

---

# Вариант 6

```python
arr = [5, 2, 9, 1, 7]

count = 0

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i] != arr[j]:
            count += 1

result = count
```

---

# Вариант 7

```python
arr = [5, 2, 9, 1, 7]

product = 1

for x in arr:
    product *= x

result = product
```

---

# Вариант 8

```python
arr = [5, 2, 9, 1, 7]

count = 0

for i in range(len(arr)):
    for j in range(len(arr)):
        for k in range(len(arr)):
            if arr[i] < arr[j] and arr[j] < arr[k]:
                count += 1

result = count
```

---

# Вариант 9

```python
arr = [5, 2, 9, 1, 7]

min_val = arr[0]

for x in arr:
    if x < min_val:
        min_val = x

result = min_val
```

---

# Вариант 10

```python
arr = [5, 2, 9, 1, 7]

sum_pairs = 0

for i in range(len(arr)):
    for j in range(len(arr)):
        sum_pairs += arr[i] * arr[j]

result = sum_pairs
```

---

# Вариант 11

```python
arr = [5, 2, 9, 1, 7]

count = 0

for x in arr:
    if x % 2 == 0:
        count += 1

result = count
```

---

# Вариант 12

```python
arr = [5, 2, 9, 1, 7]

max_diff = 0

for i in range(len(arr)):
    for j in range(len(arr)):
        diff = abs(arr[i] - arr[j])
        if diff > max_diff:
            max_diff = diff

result = max_diff
```

---

# Вариант 13

```python
arr = [5, 2, 9, 1, 7]

count = 0

for i in range(len(arr)):
    for j in range(len(arr)):
        for k in range(len(arr)):
            if arr[i] + arr[j] + arr[k] > 10:
                count += 1

result = count
```

---

# Вариант 14

```python
arr = [5, 2, 9, 1, 7]

sum_even = 0

for x in arr:
    if x % 2 == 0:
        sum_even += x

result = sum_even
```

---

# Вариант 15

```python
arr = [5, 2, 9, 1, 7]

count = 0

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i] + arr[j] > 10:
            count += 1

result = count
```

---

# Вариант 16

```python
arr = [5, 2, 9, 1, 7]

found = False

for x in arr:
    if x == 7:
        found = True

result = found
```

---

# Вариант 17

```python
arr = [5, 2, 9, 1, 7]

min_diff = 1000000

for i in range(len(arr)):
    for j in range(len(arr)):
        diff = abs(arr[i] - arr[j])
        if diff < min_diff:
            min_diff = diff

result = min_diff
```

---

# Вариант 18

```python
arr = [5, 2, 9, 1, 7]

count = 0

for x in arr:
    if x > 4:
        count += 1

result = count
```

---

# Вариант 19

```python
arr = [5, 2, 9, 1, 7]

sum_diff = 0

for i in range(len(arr)):
    for j in range(len(arr)):
        sum_diff += abs(arr[i] - arr[j])

result = sum_diff
```

---

# Вариант 20

```python
arr = [5, 2, 9, 1, 7]

count = 0

for i in range(len(arr)):
    for j in range(len(arr)):
        for k in range(len(arr)):
            if arr[i] * arr[j] * arr[k] > 20:
                count += 1

result = count
```

---

# Вариант 21

```python
arr = [5, 2, 9, 1, 7]

pairs = 0

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i] < arr[j]:
            pairs += 1

result = pairs
```

---

# Вариант 22

```python
arr = [5, 2, 9, 1, 7]

sum_pairs = 0

for i in range(len(arr)):
    for j in range(len(arr)):
        sum_pairs += arr[i] + arr[j]

result = sum_pairs
```

---

# Вариант 23

```python
arr = [5, 2, 9, 1, 7]

count = 0

for x in arr:
    if x % 3 == 0:
        count += 1

result = count
```

---

# Вариант 24

```python
arr = [5, 2, 9, 1, 7]

sum_triplets = 0

for i in range(len(arr)):
    for j in range(len(arr)):
        for k in range(len(arr)):
            sum_triplets += arr[i] * arr[j] * arr[k]

result = sum_triplets
```

---

# Вариант 25

```python
arr = [5, 2, 9, 1, 7]

count = 0

for x in arr:
    if x < 5:
        count += 1

result = count
```
