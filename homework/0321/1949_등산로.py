dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r, c, length, check):  # 시작 위치, 길이, 공사 여부 체크(안한게 True)
    global max_length
    max_length = max(max_length, length)
    
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if not (0 <= nr < N and 0 <= nc < N) or visited[nr][nc]:
            continue
        
        visited[nr][nc] = True  # 방문 체크
        
        if arr[nr][nc] < arr[r][c]:  # 낮으면 바로 이동
            dfs(nr, nc, length + 1, check)
        elif check and arr[nr][nc] - K < arr[r][c]:  # 아니면 깎고 이동
            temp = arr[nr][nc]  # 값 저장 해두기
            arr[nr][nc] = max(arr[r][c] - 1, arr[nr][nc] - K)
            dfs(nr, nc, length + 1, False)  # 공사 체크
            arr[nr][nc] = temp  # 다시 복구
            
        visited[nr][nc] = False  # 방문 해제


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())  # 한변의 길이, 최대 공사 깊이
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_height = max(map(max, arr))  # 최대 높이 찾기
    visited = [[0] * N for _ in range(N)]
    
    max_length = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == max_height:  # 최대높이인 곳에서 탐색
                visited[r][c] = 1
                dfs(r, c, 1, True)
                visited[r][c] = 0
                
    print(f'#{tc} {max_length}')