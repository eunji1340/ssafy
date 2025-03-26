import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

dp = [[-1] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]

def dfs(r, c):
    if dp[r][c] != -1:
        return dp[r][c]

    if visited[r][c]:
        return -1

    visited[r][c] = True
    max_moves = 0

    d = int(board[r][c])
    for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        nr, nc = r + dr * d, c + dc * d

        if 0 <= nr < N and 0 <= nc < M and board[nr][nc] != 'H':
            result = dfs(nr, nc)
            if result == -1:
                return -1
            max_moves = max(max_moves, result + 1)

    visited[r][c] = False
    dp[r][c] = max_moves
    return dp[r][c]

ans = dfs(0, 0)
print(ans+1 if ans != -1 else -1)
