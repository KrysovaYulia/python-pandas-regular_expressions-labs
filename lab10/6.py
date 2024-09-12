def change(matrix):
    for line2 in matrix:
        print(f'{line2[-1].ljust(2)}{" ".join(line2[1:-1]).ljust(3)} {line2[0].ljust(2)}')
f = open('Лабораторная 8.txt', encoding='utf-8')
matrix = [line.split() for line in f]
for line1 in matrix:
    print(' '.join(line1).ljust(3))
print()
print('Новая матрица')
print()
change(matrix)
