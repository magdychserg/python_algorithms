from random import random
n = round(random() * 100)
i = 1
print("The computer made a number. Guess it. You have 10 attempts. ")
while i <= 10:
    u = int(input(str(i) + ' attempts: '))
    if u > n:
        print('more')
    elif u < n:
        print('less')
    else:
        print('You guessed right with %d attempts' % i)
        break
    i += 1
else:
    print('You have exhausted 10 attempts. It was made up', n)