import re

guid_str = input()

reg = r"[0-9A-Fa-f]{8}\-[0-9A-Fa-f]{4}\-[0-9A-Fa-f]{4}\-[0-9A-Fa-f]{4}\-[0-9A-Fa-f]{12}"

reg1 = r"{[0-9A-Fa-f]{8}\-[0-9A-Fa-f]{4}\-[0-9A-Fa-f]{4}\-[0-9A-Fa-f]{4}\-[0-9A-Fa-f]{12}}"
if re.search(reg, guid_str) != None or re.search(reg1, guid_str) != None:
    print('Правильно')
else:
    print('Неправильно')