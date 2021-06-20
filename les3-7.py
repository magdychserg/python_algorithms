'''7. В одномерном массиве целых чисел определить два наименьших
элемента. Они могут быть как равны между собой (оба являться
минимальными), так и различаться.'''

import random

arr = [random.randint(0, 99) for _ in range(100)]
print(f'Массив: {arr}')

min_index_1 = 0
min_index_2 = 1

for i in arr:
    if arr[min_index_1] > i:
        min_index_2 = min_index_1
        min_index_1 = arr.index(i)
    elif arr[min_index_2] > i:
        min_index_2 = arr.index(i)

print(f'Два наименьших элемента: {arr[min_index_1]} и {arr[min_index_2]}')

'''Второй способ через сортировку списка'''

sort_list = []
sort_list.extend(arr)
sort_list.sort()

print(
    f'Два наименьших элемента (второй способ): {sort_list[0]} и {sort_list[1]}'
    )