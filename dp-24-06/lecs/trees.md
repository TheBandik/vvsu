# Деревья

## Бинарные деревья

Бинарное дерево — это иерархическая структура данных, в которой каждый узел может иметь не более двух дочерних узлов: левого и правого. Каждый дочерний узел сам по себе также является бинарным деревом. Верхний узел называется корнем, а узлы без потомков — листьями.

### Применение

Поиск и сортировка данных
Бинарные деревья поиска (BST) позволяют быстро находить, добавлять и удалять элементы. Они лежат в основе многих алгоритмов поиска и сортировки, что существенно ускоряет обработку больших объемов информации.

Организация индексов в базах данных
В реляционных СУБД (например, MySQL, PostgreSQL) используются производные бинарных деревьев (B-деревья, B+ деревья) для организации индексов и быстрого доступа к данным.

Файловые системы и иерархическое хранение
Бинарные деревья применяются для структурирования файловых систем (например, NTFS), XML-документов и других иерархических структур, что облегчает навигацию и ускоряет выполнение запросов.

Графика и 3D-сцены
В компьютерной графике бинарные деревья (например, BSP-деревья) используются для разбиения пространства, что ускоряет обработку столкновений, освещения и отрисовку объектов в 3D-играх.

Маршрутизация сетевого трафика
В сетевых устройствах бинарные деревья применяются для хранения таблиц маршрутизации, что позволяет быстро находить оптимальные пути передачи данных.

Процедурная генерация
https://www.roguebasin.com/index.php/Basic_BSP_Dungeon_generation
https://eskerda.com/demos/dungeon/

### Создание бинарного дерева

Варианты обхода:

```python
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def pre_order(node):
    if node:
        print(node.val)
        pre_order(node.left)
        pre_order(node.right)

def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.val)

def in_order(node):
    if node:
        in_order(node.left)
        print(node.val)
        in_order(node.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(5)
root.left.right = Node(7)
```

### Создание бинарного дерева поиска

```python
class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
class Tree:
    def __init__(self):
        self.root = None
    def find(self, node, parent, value):
        if node is None:
            return None, parent, False
        if value == node.val:
            return node, parent, True
        elif value < node.val:
            if node.left:
                return self.find(node.left, node, value)
        else:
            if node.right:
                return self.find(node.right, node, value)
        return node, parent, False
    def append(self, obj):
        if self.root is None:
            self.root = obj
            return obj
        s, p, fl_find = self.find(self.root, None, obj.val)
        if not fl_find and s:
            if obj.val < s.val:
                s.left = obj
            else:
                s.right = obj
        return obj
    def show(self, node):
        if node is None:
            return
        v = [node]
        while v:
            vn = []
            for x in v:
                print(x.val, end = ' ')
                if x.left:
                    vn += [x.left]
                if x.right:
                    vn += [x.right]
            print()
            v = vn
    def leaves(self, node):
        if node is None:
            return []
        v = [node]
        res = []
        while v:
            vn = []
            for x in v:
                if x.left is None and x.right is None:
                    res += [x.val]
                if x.left is not None:
                    vn += [x.left]
                if x.right is not None:
                    vn += [x.right]
            v = vn
        return res

v = [17, 6, 8, 20, 13, 11, 4, 7, 19, 100, 1, 27, 5]
t = Tree()
for val in v:
    t.append(Node(val))
print('Tree:')
t.show(t.root)
print('Leaves:')
leaves = t.leaves(t.root)
print(*leaves)
print('Max of leaves: {}, Min of leaves: {}'.format(max(leaves), min(leaves)))
```
