ln = [int(i) for i in input("Введите значения a, x, b, c:  ").split()]
a = ln[0]
b = ln[2]
c = ln[3]
x = ln[1]
y = a * x ** 2 + b * x + c
print(y)
