def change(matrix):
    c = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == n and j == m:
                matrix[n][m] = str(l)
                c += 1
                s = [print(' '.join(line5).ljust(2)) for line5 in matrix]
    if c == 0:
        print('Строка и столбец не обнаружены')

f = open('Лабораторная 8.txt', encoding='utf-8')
matrix = [line.split() for line in f]
n = int(input('Введите номер строки:  '))
m = int(input("Введите номер элемента в строке:  "))
l = int(input("Введите новое значение:  "))
print('Изначальная матрица')
a = [print(' '.join(line1).ljust(2)) for line1 in matrix]
print()
change(matrix)