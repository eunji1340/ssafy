Try = int(input())

for test_case in range(Try):
    K, N, M = map(int, input().split())
    stop_point = list(map(int, input().split()))
    stop_point.insert(0, 0)
    stop_point.insert(N - 1, N)
    print(stop_point)
    cnt, stop = 0, 0
    for i in range(1, M + 1):
        if stop_point[i] - stop_point[i - 1] > K:
            cnt = 0
            break
        elif stop_point[i + 1] - stop_point[stop] > K:
            cnt += 1
            stop = i
    print(f'#{test_case + 1} {cnt}')