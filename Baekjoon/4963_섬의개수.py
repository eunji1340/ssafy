from collections import deque

def bfs(r, c):
    global ct
    q = deque([[r, c]])
    visited[r][c] = 1
    while q:
        r, c = q.popleft()
        for dr, dc in [[0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1]]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < R and 0 <= nc < C and visited[nr][nc] == 0 and zido[nr][nc] == 1:
                q.append([nr, nc])
                visited[nr][nc] = 1
    ct += 1

while True:
    C, R = map(int, input().split())
    if C == 0 and R == 0:
        break
    zido = [list(map(int, input().split())) for _ in range(R)]
    visited = [[0] * C for _ in range(R)]
    ct = 0

    for r in range(R):
        for c in range(C):
            if zido[r][c] == 1 and not visited[r][c]:
                bfs(r, c)

    print(ct)