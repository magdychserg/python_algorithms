'''4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.'''



def foo(n, i=1, result=None):
    if result is None:
        result = []
    if n > 0:
        result.append(i)
        return foo(n - 1, -i / 2, result)
    return result


n = int(input('Enter the number of items: '))
print(foo(n))
print(sum(foo(n)))