import re

number = input()

reg = r"^[1-9]\d+"
if re.search(reg, number) and len(number) == 6:
    print('YES')
else:
    print("NO")
