def dec_to_binary(target):
    binary_number = ""

    while target > 0:
        remain = target % 2
        binary_number = str(remain) + binary_number
        target = target // 2

    print(binary_number)

def binary_to_decimal(binary_str):
    decimal_number = 0
    pow = 0

    for digit in reversed(binary_str):
        if digit == '1':
            decimal_number += 2 ** pow
            pow += 1
        else:
            pow += 1
    print(decimal_number)

def decimal_to_hexadecimal(target):
    hex_digit = "0123456789ABCDEF"
    hex_number = ""

    while target > 0:
        remain = target % 16
        hex_number = hex_digit[remain] + hex_number
        target //= 16

    print(hex_number)

dec_to_binary(149)
binary_to_decimal("10010101")
decimal_to_hexadecimal(256)





