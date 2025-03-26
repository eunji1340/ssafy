import copy
from collections import deque

def drop_blocks(copy_arr):
    for c in range(W):
        sr = H - 1
        for r in range(H):
            if copy_arr[r][c]:
                copy_arr[r][c], copy_arr[sr][c] = copy_arr[sr][c], copy_arr[r][c]
                sr -= 1

def remove_blocks(copy_arr, r, c):
    q = deque([(r, c, copy_arr[r][c])])
    copy_arr[r][c] = 0
    remove_ct = 1
    
    while q:
        r, c, power = q.popleft()
        for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            for p in range(1, power):
                nr, nc = r + dr * p, c + dc * p
                if 0 <= nr < H and 0 <= nc < W and arr[nr][nc] > 0:
                    q.append((nr, nc, copy_arr[nr][nc]))
                    copy_arr[nr][nc] = 0
                    remove_ct += 1
                    
    return remove_ct

def simulate(N, blocks):
    global min_blocks
    
    if N == 0 or blocks == 0:
        min_blocks = min(min_blocks, blocks)
        return
    
    for c in range(W):
        for r in range(H):
            if arr[r][c] > 0:
                copy_arr = copy.deepcopy(arr)
                removed_blocks = remove_blocks(copy_arr, r, c)
                drop_blocks(copy_arr)
                simulate(N - 1, blocks - removed_blocks)
                break

T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    min_blocks = 1e9
    all_blocks = 0
    
    for r in range(H):
        for c in range(W):
            if arr[r][c]:
                all_blocks += 1

    simulate(N, all_blocks)
    print(f'#{tc} {min_blocks}')