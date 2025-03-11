from collections import deque
import copy  # 깊은 복사를 위해 copy 모듈 사용


def count_blocks(arr):
    return sum(1 for r in range(H) for c in range(W) if arr[r][c] != 0)


def drop_blocks(arr):
    for c in range(W):
        stack = []
        for r in range(H):
            if arr[r][c]:
                stack.append(arr[r][c])
        for r in range(H - 1, -1, -1):
            arr[r][c] = stack.pop() if stack else 0


def remove_blocks(arr, R, C):
    dq = deque([(R, C, arr[R][C])])
    arr[R][C] = 0  # 처음 선택한 블록 제거

    while dq:
        r, c, power = dq.popleft()
        for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            for p in range(1, power):
                nr, nc = r + dr * p, c + dc * p
                if 0 <= nr < H and 0 <= nc < W and arr[nr][nc] > 0:
                    dq.append((nr, nc, arr[nr][nc]))
                    arr[nr][nc] = 0  # 블록 제거

    drop_blocks(arr)  # 블록 제거 후 아래로 정렬


def simulate(arr, N):
    global min_blocks
    if N == 0:
        min_blocks = min(min_blocks, count_blocks(arr))
        return

    for c in range(W):
        for r in range(H):
            if arr[r][c] > 0:
                temp_arr = copy.deepcopy(arr)  # 깊은 복사로 원본 유지
                remove_blocks(temp_arr, r, c)
                simulate(temp_arr, N - 1)
                break  # 한 번만 실행 후 다음 탐색


T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    min_blocks = float('inf')  # 초기화
    simulate(arr, N)

    print(f'#{tc} {min_blocks}')
