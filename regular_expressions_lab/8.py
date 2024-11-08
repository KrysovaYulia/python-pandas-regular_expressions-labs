import re

ip_ad = input()


reg = r"(([2][0-5][0-5]\.|[1][0-9][0-9]\.|[1-9][0-9]\.|[0-9]\.){3})(([2][0-5][0-5]|[1][0-9][0-9]|[1-9][0-9]|[0-9])$)"

if re.search(reg, ip_ad) != None:
    print('y')
else:
    print('n')
