def change(matrtix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = str(0)
        s = [print(' '.join(elm).ljust(3)) for elm in matrtix]
f = open('Лабораторная 8.txt', encoding='utf-8')
matrix = [line.split() for line in f]
change(matrix)
