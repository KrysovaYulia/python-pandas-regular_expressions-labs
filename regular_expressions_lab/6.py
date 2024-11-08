import re

date = input()

reg = r"(0[1-9]|[1-2]\d|3[0-1])/(0[1-9]|1[0-2])/(1[6-9]\d{2}|[2-9]\d{3})"

if re.search(reg, date) != None:
    print('y')

else:
    print('n')