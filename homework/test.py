import heapq


dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

def dijkstra():
    hq = [(0, 0, 0)]
    dists = [[float('inf')] * N for _ in range(N)]
    dists[0][0] = 0
    
    while hq:
        w, r, c = heapq.heappop(hq)
        
        if w > dists[r][c]:
            continue
        
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if not (0 <= nr < N and 0 <= nc < N):
                continue
                
            nw = w + arr[nr][nc]
            if dists[nr][nc] > nw:
                dists[nr][nc] = nw
                heapq.heappush(hq, (nw, nr, nc))
    
    return dists[N-1][N-1]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    print(f'#{tc} {dijkstra()}')