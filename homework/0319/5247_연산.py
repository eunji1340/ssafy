from collections import deque


def cal(N, M):
    q = deque([(N, 0)])
    visited = {N}

    while q:
        num, ct = q.popleft()
        if num == M:
            return ct

        for next_num in [num + 1, num - 1, num * 2, num - 10]:
            if next_num not in visited and next_num > 0 and next_num <= 1e6:
                visited.add(next_num)
                q.append((next_num, ct + 1))


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    print(f'#{tc} {cal(N, M)}')
