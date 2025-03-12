def find_path(r, c, now_sum):
    global min_sum
    
    now_sum += arr[r][c]
    
    if r == (N - 1) and c == (N - 1):   
        min_sum = min(min_sum, now_sum)
        return
    
    for dr, dc in [[0, 1], [1, 0]]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N:
            find_path(nr, nc, now_sum)
    
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 1e9
    find_path(0, 0, 0)
    print(f'#{tc} {min_sum}')