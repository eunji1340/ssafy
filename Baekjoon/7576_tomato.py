from collections import deque
from sys import stdin

def input():
    return stdin.readline().rstrip()

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    q = deque()

    for r in range(N):
        for c in range(M):
            if arr[r][c] == 1:
                q.append((r, c))

    while q:
        r, c = q.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
                arr[nr][nc] = arr[r][c] + 1
                q.append((nr, nc))


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

bfs()

result = 0
for row in arr:
    if 0 in row:
        result = 0
        break
    result = max(max(row), result)
print(result - 1)