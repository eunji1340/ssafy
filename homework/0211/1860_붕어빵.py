T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    time = list(map(int, input().split()))
    result = 'Possible'

    ct = 0  # 붕어빵 개수
    time.sort()
    bake_time = 0

    if time[0] < M:
        result = 'Impossible'
    else:
        for t in time:
            while bake_time + M <= t:
                bake_time += M
                ct += K

            if ct == 0:
                result = 'Impossible'
                break

            ct -= 1

    print(f'#{tc} {result}')