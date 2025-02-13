T = int(input())

for tc in range(1, T+1):
    N = int(input())
    n = N // 10
    floor = [[0] * n for _ in range(2)]
    print(floor)
    for i in range(2):
        for j in range(n):
            if sum(floor[i][j:j+2]) == 0:

