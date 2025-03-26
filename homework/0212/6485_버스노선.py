T = int(input())
for tc in range(1, T+1):
    N = int(input())
    bus_arr = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    C = [int(input()) for _ in range(P)]

    count = [0] * P

    for i in range(N):
        for j in range(P):
            if bus_arr[i][0] <= C[j] <= bus_arr[i][1]:
                count[j] += 1

    print(f'#{tc}', end=' ')
    print(*count)