from collections import deque
import sys
input = sys.stdin.readline

dir_map = {1: 0, 2: 1, 3: 2, 4: 3}
dr = [0, 0, 1, -1]  # 동, 서, 남, 북
dc = [1, -1, 0, 0]


def bfs(start, end):
    q = deque()
    q.append((*start, 0))  # (r, c, d, ct)
    visited = [[[0] * 4 for _ in range(N)] for _ in range(M)]
    visited[start[0]][start[1]][start[2]] = 1

    while q:
        r, c, d, ct = q.popleft()

        if [r, c, d] == end:
            return ct

        # Go 1~3칸
        for k in range(1, 4):
            nr, nc = r + dr[d] * k, c + dc[d] * k
            if not (0 <= nr < M and 0 <= nc < N):
                break
            if arr[nr][nc] == 1:  # 🔥 장애물이면 stop
                break
            if not visited[nr][nc][d]:
                visited[nr][nc][d] = 1
                q.append((nr, nc, d, ct + 1))

        # Turn: left / right (반대 방향 제외)
        for nd in range(4):
            if nd != d and nd != (d + 2) % 4:  # 반대 방향 제외
                if not visited[r][c][nd]:
                    visited[r][c][nd] = 1
                    q.append((r, c, nd, ct + 1))


M, N = map(int, input().split())  # 세로, 가로
arr = [list(map(int, input().split())) for _ in range(M)]
sr, sc, sd = map(int, input().split())
er, ec, ed = map(int, input().split())

start = [sr - 1, sc - 1, dir_map[sd]]
end = [er - 1, ec - 1, dir_map[ed]]

print(bfs(start, end))
