from collections import deque
import sys
sys.setrecursionlimit(1000000)
sys.stdin = open('input.txt', 'r')


dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c):
    if dp[r][c] != 0:
        return dp[r][c]

    dp[r][c] = 1
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < N and rooms[nr][nc] == rooms[r][c] + 1:
            dp[r][c] = max(dp[r][c], dfs(nr, nc) + 1)
    return dp[r][c]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * N for _ in range(N)]
    max_ct = 0
    room_num = N * N + 1

    for i in range(N):
        for j in range(N):
            ct = dfs(i, j)
            if max_ct < ct or (max_ct == ct and room_num > rooms[i][j]):
                max_ct = ct
                room_num = rooms[i][j]

    print(f'#{tc} {room_num} {max_ct}')

'''
#1 6 8
#2 3 2
#3 149 2
#4 2 45
#5 2 23
#6 1 2
#7 1 4
#8 5 17
#9 4 2
#10 1 35
#11 2 2
#12 7 2
#13 45 2
#14 113 2
#15 12 32
#16 6 9
#17 1 4
#18 36 42
#19 204 2
#20 7 14
#21 4 2
#22 8225 2200
#23 35 3
#24 2 2
#25 613 2
#26 33 2
#27 5 5
'''