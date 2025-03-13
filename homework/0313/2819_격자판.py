def find_number(r, c, num, ct):
    global num_set
    
    if ct == 0:
        num_set.add(num)
        return
    
    for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 4 and 0 <= nc < 4:
            find_number(nr, nc, num + str(arr[nr][nc]), ct-1)
            
T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    num_set = set()
    
    for r in range(4):
        for c in range(4):
            find_number(r, c, str(arr[r][c]), 6)
    
    print(f'#{tc} {len(num_set)}')