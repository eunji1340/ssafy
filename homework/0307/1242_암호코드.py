# import sys
# sys.stdin = open("sample_input.txt", "r")

def find_code(arr):
    code_set = set()

    for i in range(N):
        j = M - 1
        while j >= 0:
            if arr[i][j] != '0':
                sj = j
                while sj >= 0 and arr[i][sj] != '0':
                    sj -= 1
                
                code_set.add("".join(arr[i][sj + 1:j + 1]))
                j = sj
            else:
                j -= 1
                
    return list(code_set)
                
def hex_to_bin(hex_num):
    hex_digit = '0123456789ABCDEF'
    bin_code = ''
    
    for n in hex_num:
        num = hex_digit.index(n)
        bin_num = ''
        while num > 0:
            remain = num % 2
            bin_num = str(remain) + bin_num
            num //= 2
        
        while len(bin_num) < 4:
            bin_num = '0' + bin_num

        bin_code += bin_num
    
    bin_code = bin_code.strip('0')  # 앞뒤 0 지우기

    if len(bin_code) % 56 != 0:
        pow = len(bin_code) // 56 + 1
        bin_code = '0' * (56 * pow - len(bin_code)) + bin_code

    return bin_code

def match_code(bin_code):
    code = [[3, 2, 1, 1], [2, 2, 2, 1], [2, 1, 2, 2], [1, 4, 1, 1], [1, 1, 3, 2],
            [1, 2, 3, 1], [1, 1, 1, 4], [1, 3, 1, 2], [1, 2, 1, 3], [3, 1, 1, 2]]
    pow = len(bin_code) // 56

    pow_code = []
    for c in code:
        pow_code.append('0'*c[0]*pow+'1'*c[1]*pow+'0'*c[2]*pow+'1'*c[3]*pow)
    
    result = []
    for i in range(0, len(bin_code), 7*pow):
        if bin_code[i:i+7*pow] in pow_code:
            result.append(pow_code.index(bin_code[i:i+7*pow]))
    
    if not result:
        return 0

    temp1 = sum(result[i] for i in range(0, len(result) - 1, 2))  # 짝수 인덱스 (홀수번째 자리)
    temp2 = sum(result[i] for i in range(1, len(result) - 1, 2))  # 홀수 인덱스 (짝수번째 자리)
    print(result)
    if (temp1 * 3 + temp2 + result[-1]) % 10 == 0:
        return sum(result)
    else:
        return 0

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # 세로, 가로 크기
    arr = [list(input()) for _ in range(N)]  # N*M배열
    code_arr = find_code(arr)
    print(code_arr)
    bin_code = [hex_to_bin(code) for code in code_arr]
    print(bin_code)
    result = sum(match_code(code) for code in bin_code)
    
    print(f'#{tc} {result}')
    
'''
#1 38
#2 0
#3 36
#4 36
#5 44
#6 80
#7 76
#8 72
#9 182
#10 166
#11 212
#12 192
#13 1164
#14 1196
#15 1272
#16 1584
#17 4378
#18 6908
#19 7736
#20 6604

'''