def find_end(arr):
    for i in range(N):
        for j in range(M - 1, -1, -1):
            if arr[i][j] == '1':
                return i, j


def check_code(pw):
    global code
    result = []
    for i in range(0, 56, 7):
        result.append(code.index(pw[i:i + 7]))

    temp1 = temp2 = 0
    for i in range(0, len(result)):
        if i % 2 == 0:
            temp1 += result[i]
        else:
            temp2 += result[i]

    if (temp1 * 3 + temp2) % 10 == 0:
        return sum(result)
    else:
        return 0


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 세로, 가로 크기
    arr = [input() for _ in range(N)]
    code = ['0001101', '0011001', '0010011', '0111101', '0100011',
            '0110001', '0101111', '0111011', '0110111', '0001011']

    r, c = find_end(arr)
    print(f'#{tc} {check_code(arr[r][c - 55:c + 1])}')