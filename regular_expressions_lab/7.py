import re

email = input()

reg = r"[@]{1}\w+[.]{1}\w+"

if re.search(reg, email):
    print('y')
else:
    print('n')нет