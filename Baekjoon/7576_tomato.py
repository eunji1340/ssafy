from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(sr, sc):
    q = deque([(sr, sc)])
    visited[sr][sc] = 0
    day = 0

    while q:
        r, c = q.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
                if visited[nr][nc] > visited[r][c] + 1:
                    visited[nr][nc] = visited[r][c] + 1
                    q.append((nr, nc))


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[float('inf')] * M for _ in range(N)]
for r in range(N):
    for c in range(M):
        if arr[r][c] == 1:
            bfs(r, c)
print(visited)

