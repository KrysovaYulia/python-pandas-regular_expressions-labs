def calc(matrix):
    a = []
    for i in range(len(matrix)):
            s = 0
            for j in range(len(matrix[i])):
                if int(matrix[i][j]) % 2 == 0:
                    s += int(matrix[i][j])
            a.append(s)
    print(a)
f = open('Лабораторная 8.txt', encoding='utf-8')
matrix = [line.split() for line in f]
print('Изначальная матрица')
a = [print(' '.join(line1).ljust(2)) for line1 in matrix]
calc(matrix)