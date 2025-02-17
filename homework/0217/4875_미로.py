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
        stack = []
        while 0 <= r < N and 0 <= c < N:
            for dr, dc in [[0, 1], [-1, 0], [0, -1]]:
                if maze[r + dr][c + dc] != 0:
                    r = r + dr
                    c = c + dc
                    stack.append([r, c])
                    break
            else:
                return 0
            if maze[r][c] == 2:
                return 1
        return 0

    print(f'#{tc} {find_path(r, c, maze)}')