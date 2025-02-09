for tc in range(1, 11):
    num = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    Max = 0

    # 가로줄
    for i in range(100):
        if Max < sum(arr[i]):
            Max = sum(arr[i])

    # 세로줄
    for c in range(100):
        col_sum = sum(arr[r][c] for r in range(100))
        if Max < col_sum:
            Max = col_sum

    # 대각선1
    diag1 = 0
    for i in range(100):
        for j in range(100):
            if i == j:
                diag1 += arr[i][j]

    # 대각선2
    diag2 = 0
    for i in range(100):
        for j in range(100):
            if (i + j) == 99:
                diag2 += arr[i][j]

    Max = max(Max, diag1, diag2)

    print(f'#{num} {Max}')


    # # 강사님 코드
    #
    # max_val = 0
    #
    # # 가로줄 합 구하기
    # for r in range(100):
    #     max_val = max(max_val, sum(arr[r]))
    #
    # # 세로줄 합 구하기
    # for c in range(100):
    #     col_sum = sum(arr[r][c] for r in range(100))
    #     max_val = max(max_val, col_sum)
    #
    #
    # # 대각선 1
    # diag1_sum = sum(arr[i][i] for i in range(100))
    # max_val = max(max_val, diag1_sum)
    #
    # # 대각선 2
    # diag2_sum = sum(arr[i][99-i] for i in range(100))
    # max_val = max(max_val, diag2_sum)
