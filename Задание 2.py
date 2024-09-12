st = input('Введите числа:  ').split()
ch = 0
nch = 0
for i in st:
    if int(i) % 2 == 0:
        ch += 1
    else:
        nch += 1
if ch == 3:
    print('WIN')
elif nch == 3:
    print('WIN')
else:
    print('FAIL')