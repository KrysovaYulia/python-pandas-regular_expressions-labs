def dlt(martix):
    k = 0
    for line in martix[:-4]:
        print(' '.join(line).ljust(3))
        k += 1
    print(f'Стало {k} строк')
f = open('Лабораторная 8.txt', encoding='utf-8')
c = 0
matrix = [line.split() for line in f]
for sp in matrix:
    c += 1
print(f'Было {c} строк')
dlt(matrix)