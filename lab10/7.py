def calculate(matrix):
    global number
    c = 0
    for line in matrix:
        for elemnt in line:
            if number == int(elemnt):
                c += 1
    if c != 0:
        print(c)
    else:
        print('Такого числа нет')
f = open('Лабораторная 8.txt', encoding='utf-8')
matrix = [line.split() for line in f]
number = int(input('Введите число  '))
calculate(matrix)