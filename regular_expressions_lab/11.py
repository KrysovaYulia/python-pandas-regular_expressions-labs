import re

list_price = "Текст с ценами: 23.78 USD, 22 UDD, 53.95 EU, 0.002 USD, 00.02 US, 89.31 RUR, 65 RUR 1.9 EU 9.32 USD"




reg = r"([1-9][0-9]+( USD| RUR| EU))|([0-9]+\.[0-9]{1}( USD| RUR| EU){1})|([0-9]+\.[0-9]{,2}( USD| RUR| EU){1})|([0-9]\.[0-9]{,2}( USD| RUR| EU){1})"

d = ([x.group() for x in re.finditer(reg, list_price)])


print(d)