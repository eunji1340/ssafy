from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))

    # front = 0
    # for i in range(M):
    #     queue.append(queue[front])
    #     front += 1
    #
    # print(f'#{tc} {queue[front]}')

    q = deque()
    q.extend(queue)

    for _ in range(M):
        q.append(q.popleft())

    print(f'#{tc} {q.popleft()}')
