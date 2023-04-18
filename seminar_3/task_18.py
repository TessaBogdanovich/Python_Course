## Задача 18: Требуется найти в массиве A[1..N] самый близкий по
## величине элемент к заданному числу X. Пользователь в первой строке
## вводит натуральное число N – количество элементов в массиве. В
## последующих строках записаны N целых чисел Ai
## . Последняя строка содержит число X

## 5
## 1 2 3 4 5
## 6
## -> 5

import random
import math

N = int(input("Введите количество элементов: "))
array = []
minarr = int(input("Введите нижний порог значений в массиве: "))
maxarr = int(input ("Введите верхний порог значчений в массиве: "))
x = int(input("Введите искомое число: "))
for i in range(N):
    array.append(random.randint(minarr, maxarr))
result = array[0]
eps = x
for i in array:
    if abs (i - x) < eps:
        eps = abs (i - x)
        result = 1
print (array)

print (result)
