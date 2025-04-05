# Лабораторная работа №7

Каждому студенту предлагается один из следующих вариантов. Для каждого алгоритма необходимо:
- Построить блок-схему
- Оценить сложность алгоритма

# Вариант 1

```python
n = 28
result = [i for i in range(1, n+1) if n % i == 0]
```

# Вариант 2

```python
arr = [1, 2, 3]
result = [x * i for i, x in enumerate(arr)]
```

# Вариант 3

```python
s = "abcabcbb"
seen = {}
start = max_length = 0
for i, c in enumerate(s):
    if c in seen and seen[c] >= start:
        start = seen[c] + 1
    seen[c] = i
    max_length = max(max_length, i - start + 1)
result = max_length
```

# Вариант 4

```python
arr = [2, 4, 6]
result = all(x % 2 == 0 for x in arr)
```

# Вариант 5

```python
n = "12345"
result = sum(int(digit) for digit in str(n))
```

# Вариант 6

```python
def matrix_multiply(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result
result = matrix_multiply([[1]], [[2]])
```

# Вариант 7

```python
def subsets(arr):
    result = [[]]
    for num in arr:
        result += [curr + [num] for curr in result]
    return result
result = subsets([1, 2])
```

# Вариант 8

```python
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
result = linear_search([1, 2, 3], 2)
```

# Вариант 9

```python
k = 3
arr = [3, 6, 7]
remainders = {x % k for x in arr}
result = len(remainders) < len(arr)
```

# Вариант 10

```python
def max_subarray_sum(arr):
    if len(arr) == 0:
        return float('-inf')
    return max(max_subarray_sum(arr[:-1]), sum(arr))

arr = [-2, -3, -1]
result = max_subarray_sum(arr)
```
