def bfs(i, j, N):
    visited = [[0] * N for _ in range(N)]
    q = [[i, j]]
    visited[i][j] = 1

    while q:
        ti, tj = q.pop(0)
        if maze[ti][tj] == 3:
            return 1
        for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
            wi, wj = ti+di, tj+dj
            if 0 <= wi < N and 0 <= wj < N and maze[wi][wj] != 1 and visited[wi][wj] == 0:
                q.append([wi, wj])
                visited[wi][wj] = 1

    return 0

def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j

for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]  # 16*16. 출발=2, 도착=3
    sti, stj = find_start(16)
    ans = bfs(sti, stj, 16)
    print(f'#{tc} {ans}')