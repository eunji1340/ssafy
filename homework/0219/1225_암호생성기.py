from collections import deque

for tc in range(10):
    N = int(input())
    queue = deque(list(map(int, input().split())))

    num = 1
    while True:
        queue.append(queue.popleft() - num)
        if queue[-1] <= 0:
            queue[-1] = 0
            break
        num = num % 5 + 1

    print(f'#{N}', end=' ')
    print(*queue)