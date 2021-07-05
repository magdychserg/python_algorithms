'''Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
 Найти в массиве медиану. Медианой называется элемент ряда, делящий его на две
 равные части: в одной находятся элементы, которые не меньше медианы, в другой – не больше ее.'''

import random

size = 8

lst = [random.randint(0, 100) for _ in range(2 * size + 1)]

def sort(lst):
    i = 1
    while i < len(lst):

        if lst[i - 1] <= lst[i]:
            i += 1
        else:
            lst[i], lst[i - 1] = lst[i - 1], lst[i]
            i -= 1
            if i == 0:
                i = 1

    return lst

print(f'Исходный массив:\n{lst}')
print(f'Медиана: {sort(lst)[len(lst) // 2]}')
