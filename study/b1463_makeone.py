from collections import deque

N = int(input())

def bfs():
    q = deque([N])
    visited = [0] * (N + 1)

    while q:
        n = q.popleft()
        if n == 1:
            return visited[n]
        if n % 3 == 0 and not visited[n // 3]:
            visited[n // 3] = visited[n] + 1
            q.append(n // 3)
        if n % 2 == 0 and not visited[n // 2]:
            visited[n // 2] = visited[n] + 1
            q.append(n // 2)
        if not visited[n - 1]:
            visited[n - 1] = visited[n] + 1
            q.append(n - 1)


print(bfs())