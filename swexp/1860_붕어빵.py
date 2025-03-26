T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    time = list(map(int, input().split()))
    people = [0] * (max(time) + 1)  # 인덱스=시간, 값=사람수
    result = 'Possible'

    for i in range(N):
        people[time[i]] += 1

    ct = 0  # 붕어빵 개수
    now_time = 0
    while now_time <= max(time):  # 붕어빵이 있을 때
        if now_time % M == 0 and now_time != 0:
            ct += K
        ct -= people[now_time]

        if ct < 0:
            result = 'Impossible'
            break

        now_time += 1

    print(f'#{tc} {result}')