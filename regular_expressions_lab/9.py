import re

password = input()

reg = r"([a-z]+)([A-Z]+)([0-9]+)(_*)"


if re.search(reg, password) and len(password) >= 8:
    print('YES')
else:
    print('NO')