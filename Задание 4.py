a = int(input("Введите число в двочиной системе счисления:  "))
b = int(input("Введите число в двочиной системе счисления:  "))

def bin1(binnum):
    lstbin = []
    for i in range(len(str(binnum))):
        bin_dec = int(str(binnum)[-1 + i]) * 2 ** i
        lstbin.append(bin_dec)
    return sum(lstbin)


def dec1(sum_dec):
    sumd = sum_dec
    sum_bin = ''
    while sumd > 0:
        new_bin = sumd % 2
        sum_bin += str(new_bin)
        sumd //= 2
    return sum_bin[::-1]
sum_dec = bin1(a) + bin1(b)
print(dec1(sum_dec))
