def find_room(r, c):
    global max_ct, room_num
    
    start_room = arr[r][c]
    ct = 1
    stack = [(r, c, ct)]
    
    while stack:
        r, c, ct = stack.pop()
        
        if max_ct < ct or (max_ct == ct and room_num > start_room):
            max_ct = ct
            room_num = arr[r][c]
        
        for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and arr[r][c] == arr[nr][nc] + 1:
                stack.append((nr, nc, ct + 1))
    
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_ct = 0
    room_num = 1e9
    
    for r in range(N):
        for c in range(N):
            find_room(r, c)
            
    print(f'#{tc} {room_num} {max_ct}')