import heapq

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dijkstra(sr, sc):
    pq = [[0, sr, sc]]
    visited = [[float('inf')] * N for _ in range(N)]
    visited[sr][sc] = 0
    
    while pq:
        w, r, c = heapq.heappop(pq)
        
        if visited[r][c] < w:
            continue
        
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if not (0 <= nr < N and 0 <= nc < N):
                continue
                
            nw = w + 1
            if arr[nr][nc] > arr[r][c]:
                nw += (arr[nr][nc] - arr[r][c])
            
            if visited[nr][nc] > nw:
                visited[nr][nc] = nw
                heapq.heappush(pq, (nw, nr, nc))
    
    return visited[N-1][N-1]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {dijkstra(0, 0)}')