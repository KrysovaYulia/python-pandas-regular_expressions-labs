import re

hex_number = input()
reg = r"^#[0-9A-F]{5}"
if re.findall(reg, hex_number) and len(hex_number) == 7:
    print('YES')
else:
    print('NO')