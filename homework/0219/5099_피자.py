from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # N = 화덕의크기, M = 피자 개수
    cheeses = list(map(int, input().split()))  # 치즈 양
    pizza = deque(zip(range(1, M+1), cheeses))  # (피자번호, 치즈 양)
    q = deque()  # 화덕

    # 처음에 집어넣기
    for _ in range(N):
        q.append(pizza.popleft())

    # 다 구워질때까지
    num = cheese = 0
    while len(q) > 0:
        num, cheese = q.popleft()
        cheese //= 2

        if cheese == 0 and pizza:
            q.append(pizza.popleft())
        elif cheese > 0:
            q.append((num, cheese))

    print(f'#{tc} {num}')