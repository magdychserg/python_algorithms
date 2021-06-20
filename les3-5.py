'''5. В массиве найти максимальный отрицательный элемент. Вывести на
экран его значение и позицию в массиве.'''

import random

arr = [random.randint(-99, 99) for _ in range(100)]
print(arr)

i = 0
max_index = -1
for i in arr:
    if arr[i] < 0 and max_index == -1:
        max_index = i
    elif arr[i] < 0 and arr[i] > arr[max_index]:
        max_index = i
    i += 1
if arr[max_index] >= 0:
    print(f'В массиве нет отрицательных элементов')
else:
    print(f'В массиве максимальный отрицательный элемент: {arr[max_index]}.',
      f'Находится в массиве на позиции {max_index + 1}')