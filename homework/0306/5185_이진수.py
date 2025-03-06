def hex_to_bin(num):
    global result, hex_digit
    bin_num = ''
    num = hex_digit.index(num)
    while num > 0:
        remain = num % 2
        bin_num = str(remain) + bin_num
        num //= 2
    
    while len(bin_num) < 4:
        bin_num = '0' + bin_num
    
    result += bin_num

T = int(input())
for tc in range(1, T+1):
    N, hex_num = input().split()
    hex_digit = '0123456789ABCDEF'
    result = ''
    
    for digit in hex_num:
        hex_to_bin(digit)
        
    print(f'#{tc} {result}')
