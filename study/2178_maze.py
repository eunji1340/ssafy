from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    q = deque([(0, 0)])
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1

    while q:
        r, c = q.popleft()

        if r == N - 1 and c == M - 1:
            return visited[r][c]

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and maze[nr][nc] == 1:
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr, nc))

print(bfs())