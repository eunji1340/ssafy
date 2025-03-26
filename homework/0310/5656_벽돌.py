from collections import deque
import copy

def count_blocks(arr):  # 블럭 수 세기
    blocks = 0
    for r in range(H):
        for c in range(W):
            if arr[r][c] != 0:
                blocks += 1
    return blocks  # 블럭 수 리턴

def drop_blocks(arr):  # 블럭 떨구기
    for c in range(W):
        idx = H-1  # 맨 아래에서 부터 시작
        for r in range(H-1, -1, -1):
            if arr[r][c]:  # 0이 아니라면 맨 아래에서 부터 자리 바꾸기
                arr[r][c], arr[idx][c] = arr[idx][c], arr[r][c]
                idx -= 1  # 한칸씩 올리기

def remove_blocks(arr, R, C):  # 블럭 지우기
    dq = deque([(R, C, arr[R][C])])  # q에 지울 블럭 r,c,폭발범위 넣기
    arr[R][C] = 0  # 블럭 지우기
    
    while dq:
        r, c, power = dq.popleft()  # 큐에서 빼오기
        
        for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:  # 상하좌우 bomb
            for p in range(1, power):  # power크기만큼
                nr, nc = r + dr * p, c + dc * p
                if 0 <= nr < H and 0 <= nc < W and arr[nr][nc] > 0:  # 범위검사 & 블럭확인
                    dq.append((nr, nc, arr[nr][nc]))
                    arr[nr][nc] = 0

    drop_blocks(arr)  # 다 지웠으니 블럭 정렬

def simulate(arr, N):
    global min_blocks
    
    blocks = count_blocks(arr)  # 현재 배열의 블럭 수
    
    if N == 0 or blocks == 0:  # 횟수를 다 썼거나 블럭 수가 이미 0이라면 멈추기
        min_blocks = min(min_blocks, blocks)  # 최솟값을 저장하고 리턴
        return min_blocks
    
    for c in range(W):
        for r in range(H):
            if arr[r][c] > 0:  # 블럭이 있다면 (= 0이 아니라면)
                temp_arr = copy.deepcopy(arr)  # 배열 복사해오기
                remove_blocks(temp_arr, r, c)  # 복사한 배열로 블럭 지우기
                simulate(temp_arr, N-1)  # 횟수 -1하고 다시 시뮬돌리기
                break  # 다음 열로 이동

T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())  # 횟수, W*H 배열
    arr = [list(map(int, input().split())) for _ in range(H)]
    min_blocks = 1e9  # 남은 블럭 수 중 최솟값을 저장
    simulate(arr, N)  # 시뮬 돌리기
    
    print(f'#{tc} {min_blocks}')