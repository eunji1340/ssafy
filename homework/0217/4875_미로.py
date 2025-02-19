T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 미로의 크기
    maze = [list(map(int, input())) for _ in range(N)]
    r, c = 0, 0

    # 도착 지점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 3:
                r = i
                c = j

    def find_path(r, c, maze):
        stack = [(r, c)]
        while stack:
            r, c = stack.pop()
            if maze[r][c] == 2:
                return 1
            if maze[r][c] == 0:
                maze[r][c] = 1

            for dr, dc in [[0, 1], [-1, 0], [0, -1], [1, 0]]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] != 1:
                    stack.append((nr, nc))

        return 0

    print(f'#{tc} {find_path(r, c, maze)}')