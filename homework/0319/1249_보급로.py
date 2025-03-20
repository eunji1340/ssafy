from collections import deque


def bfs():
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    
    min_time[0][0] = arr[0][0]
    q = deque([(0, 0)])
    
    while q:
        r, c = q.popleft()
        
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                now_time = min_time[r][c] + arr[nr][nc]
                if now_time < min_time[nr][nc]:
                    min_time[nr][nc] = now_time
                    q.append((nr, nc))
    
    return min_time[N-1][N-1]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]
    min_time = [[float('inf')] * N for _ in range(N)]
    
    print(f'#{tc} {bfs()}')
