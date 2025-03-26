def bfs(si, sj, N):
    q = [[si, sj]]
    visited = [[0] * N for _ in range(N)]
    visited[si][sj] = 0
    while q:
        i, j = q.pop()
        if maze[i][j] == 3:
            return visited[i][j] - 1
        for di, dj in [[0, 1], [-1, 0], [0, -1], [1, 0]]:
            wi, wj = i + di, j + dj
            if 0 <= wi < N and 0 <= wj < N and maze[wi][wj] != 1 and visited[wi][wj] == 0:
                q.append([wi, wj])
                visited[wi][wj] = visited[i][j] + 1
    return 0

def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    si, sj = find_start(N)
    print(f'#{tc} {bfs(si, sj, N)}')