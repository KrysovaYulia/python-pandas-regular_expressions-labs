import re

password = ['(3+5)-9*4', '(2*9)-6*5', '(16+3)-5+4', '(4*9)+2*4']

reg = r"([0-9]\+)+"

for i in password:
    if re.search(reg, i) != None:
        print(f'{i}: правильное выражение')
    else:
        print(f'{i}: неправильное выражение')
