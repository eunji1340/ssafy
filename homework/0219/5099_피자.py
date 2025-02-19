from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cheeses = list(map(int, input().split()))
    nums = list(range(1, M+1))
    pizzas = list(zip(nums, cheeses))

    q = deque()

    for _ in range(N):
        q.append(pizzas.pop(0))

    while len(q) > 1:
        num, cheese = q.popleft()
        cheese //= 2

        if cheese == 0 and pizzas:
            q.append(pizzas.pop(0))
        elif cheese > 0:
            q.append((num, cheese))

    num, cheese = q.popleft()

    print(f'#{tc} {num}')
