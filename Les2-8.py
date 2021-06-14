'''8. Посчитать, сколько раз встречается определенная цифра в введенной
последовательности чисел. Количество вводимых чисел и цифра, которую необходимо
посчитать, задаются вводом с клавиатуры.'''


user_range = input('Enter the sequence: ')
user_patten = input('Enter a number to search for: ')
count = 0

for i in user_range:
    if i == user_patten:
        count += 1

print(f'In a given sequence {user_range}, the number {user_patten} occurs {count} times')