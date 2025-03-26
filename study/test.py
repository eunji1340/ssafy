import heapq

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dijkstra():
    q = [(0, 0, 0)]
    dists = [[float('inf')] * N for _ in range(N)]
    dists[0][0] = 0

    while q:
        w, r, c = heapq.heappop(q)
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if not(0 <= nr < N and 0 <= nc < N):
                continue
            nw = dists[r][c] + dists[nr][nc]
            if dists[nr][nc] <= nw:
                continue
            if nr == N - 1 and nc == N - 1:
                return nw

            dists[nr][nc] = nw
            heapq.heappush(q, (nw, nr, nc))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = dijkstra()
    print(f'#{tc} {result}')
