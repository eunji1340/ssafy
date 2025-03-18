def check(row, col):
    for i in range(row):
        if visited[i][col]:
            return False

    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if visited[i][j]:
            return False
        i -= 1
        j -= 1


def dfs(row):
    global answer
    if row == N:
        answer += 1
        return

    for col in range(N):
        if check(row, col) is False:
            continue

        visited[row][col] = 1
        dfs(row + 1)
        visited[row][col] = 0


N = 4
visited = [[0] * N for _ in range(N)]
answer = 0

dfs(0)
print(answer)