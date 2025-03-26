def select_item(row, total):
    global min_cost
    if total > min_cost:
        return
    
    if row == N:
        min_cost = min(min_cost, total)
        return
        
    for col in range(N):
        if not visited[col]:
            visited[col] = 1
            select_item(row + 1, total + V[row][col])
            visited[col] = 0
            

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]
    min_cost = 1e9
    visited = [0] * (N + 1)
    select_item(0, 0)
    print(f'#{tc} {min_cost}')