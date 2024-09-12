def sqrt1(matrix):
        c = 0
        a = []
        for line2 in matrix:
            if c < 4:
                a.append([(int(elmnt) ** 2) for elmnt in line2])
                c += 1
            else:
                a.append([int(elmnt) for elmnt in line2])
        print('Новая матрица')
        for elm in a:
            print(' '.join([str(elm2).ljust(3) for elm2 in elm]))
f = open('Лабораторная 8.txt', encoding='utf-8')
matrix = [line.split() for line in f]
print('Изначальная матрица')
a = [print(' '.join(line1).ljust(2)) for line1 in matrix]
sqrt1(matrix)
