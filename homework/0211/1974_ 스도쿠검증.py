T = int(input())

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = 1

    # 가로줄 검사
    for i in range(9):
        if sorted(arr[i]) != list(range(1, 10)):
            result = 0

    # 세로줄 검사
    for c in range(9):
        temp = []
        for r in range(9):
            temp.append(arr[r][c])
        if sorted(temp) != list(range(1, 10)):
            result = 0

    # 3*3 검사
    for c in range(0, 9, 3):
        for r in range(0, 9, 3):
            temp = []
            for i in range(c, c+3):
                for j in range(r, r+3):
                    temp.append(arr[i][j])
            if sorted(temp) != list(range(1, 10)):
                result = 0

    print(f'#{tc} {result}')
