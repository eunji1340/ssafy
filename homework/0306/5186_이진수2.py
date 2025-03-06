def dec_to_bin(dec_num):
    bin_num = ''
    pow = -1
    while dec_num > 0:
        if dec_num - 2 ** pow >= 0:
            bin_num += '1'
            dec_num -= 2 ** pow
        else:
            bin_num += '0'

        pow -= 1

    if len(bin_num) < 13:
        return bin_num
    else:
        return 'overflow'


T = int(input())
for tc in range(1, T + 1):
    N = float(input())

    print(f'#{tc} {dec_to_bin(N)}')