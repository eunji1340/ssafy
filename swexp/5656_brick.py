import copy

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

def find_top(c, now_arr):
    for r in range(H):
        if now_arr[r][c] != 0:
            return r, c
    return None

def bomb_brick(r, c, copy_arr):
    power = copy_arr[r][c]
    copy_arr[r][c] = 0
    for d in range(4):
        for m in range(1, power):
            nr, nc = r + dr[d] * m, c + dc[d] * m
            if not (0 <= nr < H and 0 <= nc < W) or copy_arr[nr][nc] == 0:
                continue
            bomb_brick(nr, nc, copy_arr)
    return copy_arr

def count_brick(now_arr):
    return sum(1 for r in range(H) for c in range(W) if now_arr[r][c])

def drop_brick(copy_arr):
    for c in range(W):
        stack = []
        for r in range(H-1, -1, -1):
            if copy_arr[r][c] != 0:
                stack.append(copy_arr[r][c])
        for r in range(H-1, -1, -1):
            if stack:
                copy_arr[r][c] = stack.pop(0)
            else:
                copy_arr[r][c] = 0
    return copy_arr

def drop(ct, now_arr):
    global min_brick

    remain = count_brick(now_arr)
    if remain == 0:
        min_brick = 0
        return

    if ct == N:
        min_brick = min(min_brick, count_brick(now_arr))
        return

    for col in range(W):
        top = find_top(col, now_arr)
        if top is None:
            continue
        sr, sc = top
        bomb_arr = bomb_brick(sr, sc, copy.deepcopy(now_arr))
        drop_arr = drop_brick(bomb_arr)
        drop(ct + 1, drop_arr)

T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    min_brick = float('inf')
    drop(0, arr)
    print(f'#{tc} {min_brick}')
