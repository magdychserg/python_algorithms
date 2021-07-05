'''1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный
массив, заданный случайными числами на промежутке [-100; 100). Выведите на
экран исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).'''

import random


size = 20

random_lst = [random.randint(-100, 99) for i in range(size)]


def bubble_sort(numb_array):
    a = numb_array

    len_array = len(a)
    for i in range(len_array - 1):
        counter = 0
        for j in range(len_array - 1 - i):
            if a[j] < a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                counter += 1
        if counter == 0:
            break
    return a


print(f'Исходный массив:\n{random_lst}\n')
print(f'Сортированный массив:\n{bubble_sort(random_lst)}')