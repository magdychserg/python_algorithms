"""1. Найти сумму и произведение цифр трехзначного числа,
    которое вводит пользователь."""

number = input('Введите трехзначное число: ')

sum_number = 0
prod_number = 1

for i in number:
    sum_number += int(i)
    prod_number *= int(i)
print(f"Сумма цифр числа {number}: {sum_number}")
print(f"Произведение цифр: {number}: {prod_number}")