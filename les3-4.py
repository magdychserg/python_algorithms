'''4. Определить, какое число в массиве встречается чаще всего.'''

import random
kol_number = 30
arr = [random.randint(0, 30) for _ in range(kol_number)]
print(f'Массив: {arr}')

num = arr[0]
max_frq = 1
for i in range(kol_number):
    frq = 1
    for k in range(i + 1, kol_number):
        if arr[i] == arr[k]:
            frq += 1
    if frq > max_frq:
        max_frq = frq
        num = arr[i]

if max_frq > 1:
    print(f'Чаще всего встречается число {num} - {max_frq} раз(а)')
else:
    print('Все элементы уникальны')