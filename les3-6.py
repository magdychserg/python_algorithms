'''6. В одномерном массиве найти сумму элементов, находящихся между
минимальным и максимальным элементами. Сами минимальный и максимальный
элементы в сумму не включать.'''

import random

arr = [random.randint(0, 99) for _ in range(10)]
print(f'Массив: {arr}')

min_index = 0
max_index = 0
step = 1
sum = 0

for i in arr:
    if arr[min_index] > i:
        min_index = arr.index(i)
    elif arr[max_index] < i:
        max_index = arr.index(i)

if max_index - min_index < 0:
    step = -1

for i in arr[min_index + step:max_index:step]:
    sum += i


print(
        f'Сумма элементов между минимальным ({arr[min_index]})',
        f' и максимальным ({arr[max_index]}) элементами: {sum}'
        )