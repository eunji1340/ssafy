from collections import deque

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    cheese = deque(list(map(int, input().split())))
    q = deque([0] * N)
    result = 0

    i = 0
    num = 1  # 피자 번호
    count = 0  # 완성된 피자 개수

    while count > 0 or cheese:
        if q[i] == 0 and cheese: # 제일 처음에 피자 넣기
            q[i] = [cheese.popleft(), num]
            num += 1
            count += 1
        elif q[i] != 0:  # 피자가 이미 들어 있다면
            q[i][0] //= 2
            if q[i][0] == 0 and cheese:
                q[i] = [cheese.popleft(), num]
                num += 1
                count += 1
            elif q[i][0] == 0 and not cheese:
                count -= 1
                result = q[i][1]

        i = (i + 1) % N

    print(f'#{tc} {result}')