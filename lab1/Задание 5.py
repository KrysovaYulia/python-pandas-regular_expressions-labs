import random

s = input('Введите строку:  ')
f = input("Введите дополнительную букву:   ")
s_rand = s + f

lsts = [i for i in s_rand]
rands = random.shuffle(lsts)

t = ''.join(lsts)

for ltr in t:
    if ltr in s:
        if s.count(ltr) < t.count(ltr):
            print(f'Лишняя буква: {ltr}')
            break
    else:
        print(f'Лишняя буква: {ltr}')
