import re

str_1 = input()

reg = r"abcdefghijklmnopqrstuv18340"

if re.search(reg, str_1) != None:
    print('Строка правильная')
else:
    print('Строка неправильная')