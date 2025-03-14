import sys
from collections import deque
#sys.stdin = open('input.txt', 'r')

directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

def dfs(sr, sc, r, c, visited, direction, count):
    global max_ct
    
    if direction == 3 and (r, c) == (sr, sc) and count > 3:
        max_ct = max(max_ct, count)
        return
        
    for i in range(direction, 4):
        nr, nc = r + directions[i][0], c + directions[i][1]
        
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] not in visited:
            visited.add(arr[nr][nc])
            dfs(sr, sc, nr, nc, visited, i, count + 1)
            visited.remove(arr[nr][nc])
        
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_ct = -1
    
    for r in range(0, N-1):
        for c in range(1, N-1):
            dfs(r, c, r, c, set([arr[r][c]]), 0, 1)
            
    print(f'#{tc} {max_ct}')
'''
1          
4                
9 8 9 8
4 6 9 4
8 7 7 8
4 5 3 5
'''