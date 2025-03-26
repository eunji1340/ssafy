# def dec_to_bin(dec_num):
#     bin_num = ''
#     pow = -1
#     while dec_num > 0:
#         if dec_num - 2 ** pow >= 0:
#             bin_num += '1'
#             dec_num -= 2 ** pow
#         else:
#             bin_num += '0'
# 
#         pow -= 1
# 
#     if len(bin_num) < 13:
#         return bin_num
#     else:
#         return 'overflow'
# 
# 
# T = int(input())
# for tc in range(1, T + 1):
#     N = float(input())
# 
#     print(f'#{tc} {dec_to_bin(N)}')
def dec_to_bin(dec_num):
    bin_num = ''
    pow = -1
    while dec_num > 0:
        if dec_num < 2 ** pow:
            bin_num += '0'
        else:
            bin_num += '1'
            dec_num -= 2 ** pow
        pow -= 1
    
    if len(bin_num) > 12:
        return 'overflow'
    
    return bin_num
        
T = int(input())
for tc in range(1, T+1):
    N = float(input())
    print(f'#{tc} {dec_to_bin(N)}')
    
'''
T = int(input())
for tc in range(1, T+1):
    N = float(input())
    result = ''
 
    for i in range(1, 13): # 12번 반복
        if not N: # N이 0이 되면 break
            break
        N *= 2
        if N >= 1: # 1보다 크다면 1 추가
            result += '1'
            N -= 1
            continue
        result += '0'
 
    print(f'#{tc} {result if not N else "overflow"}')
    # N이 아직도 0이 되지 않았다면, 즉 소수점 아래가 13자리가 넘어간다면 overflow
'''