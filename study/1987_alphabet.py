from collections import deque
from sys import stdin
def input():
    return stdin.readline().rstrip()

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

'''
def bfs(R, C):
    global result
    q = deque([(0, 0, board[0][0])])

    while q:
        r, c, alpha = q.popleft()
        result = max(result, len(alpha))
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < R and 0 <= nc < C and board[nr][nc] not in alpha:
                q.append((nr, nc, alpha+board[nr][nc]))
'''

def dfs(r, c, path):
    global result
    result = max(result, len(path))
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < R and 0 <= nc < C and board[nr][nc] not in path:
            path.add(board[nr][nc])
            dfs(nr, nc, path)
            path.remove(board[nr][nc])


R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
result = 0
#bfs(R, C)
dfs(0, 0, set(board[0][0]))
print(result)