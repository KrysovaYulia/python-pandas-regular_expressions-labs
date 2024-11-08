import re

mac_ad = input()

reg = r'([0-9A-Fa-f]{2}\:){5}([0-9A-Fa-f]{2})$'


if re.search(reg, mac_ad) != None:
    print('YES')
else:
    print('NO')