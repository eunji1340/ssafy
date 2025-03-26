from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
types = {
    1: [1, 1, 1, 1],
    2: [1, 1, 0, 0],
    3: [0, 0, 1, 1],
    4: [1, 0, 0, 1],
    5: [0, 1, 0, 1],
    6: [0, 1, 1, 0],
    7: [1, 0, 1, 0]
}

def bfs(R, C):
    ct = 0
    q = deque([(R, C)])
    visited[R][C] = 1
    
    while q:
        r, c = q.popleft()
        d = types[tunnel[r][c]]
        
        if visited[r][c] <= L:
            ct += 1
        
        for i in range(4):
            if d[i] == 0:  # 나갈 방향이 없으면
                continue

            nr, nc = r + dr[i], c + dc[i]
            
            if nr < 0 or nr >= N or nc < 0 or nc >= M:  # 인덱스 범위 체크
                continue
            
            if visited[nr][nc] != 0 or tunnel[nr][nc] == 0:  # 방문했거나 갈 수 없으면
                continue
                
            nd = types[tunnel[nr][nc]]
            
            # 현재 상, 좌 일 때 다음 파이프가 하,우가 안뚫렸으면
            if i % 2 == 0 and nd[i+1] == 0:
                continue
            # 현재 하, 우 일 때 다음 파이프가 상,좌가 안뚫렸으면
            if i % 2 == 1 and nd[i-1] == 0:
                continue
            
            if visited[nr][nc] + 1 > L:
                continue
                
            visited[nr][nc] = visited[r][c] + 1
            q.append((nr, nc))

    return ct

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
        
    print(f'#{tc} {bfs(R, C)}')