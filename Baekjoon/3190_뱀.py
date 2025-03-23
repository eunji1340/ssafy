import sys
from collections import deque
#sys.stdin = open('input.txt', 'r')

# 오른쪽(0), 아래(1), 왼쪽(2), 위(3)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def simul():
    snake = deque([(0, 0)])  # 뱀 위치 (머리가 마지막)
    now_time = 0  # 현재 시간
    now_dirs = 0  # 현재 뱡항 (초기값 : 오른쪽)

    while True:
        now_time += 1
        r, c = snake[-1]  # 현재 머리 위치
        nr, nc = r + dr[now_dirs], c + dc[now_dirs]  # 머리 이동 위치

        # 벽 또는 자기 자신과 충돌하면 종료
        if not (0 <= nr < N and 0 <= nc < N) or (nr, nc) in snake:
            return now_time

        # 사과가 있으면 길이 유지, 없으면 꼬리 제거
        if board[nr][nc] == 1:
            board[nr][nc] = 0
        else:
            snake.popleft()

        snake.append((nr, nc))  # 머리 추가

        if now_time in turn_dict:  # 방향 전환 확인
            if turn_dict[now_time] == 'L':  # 왼쪽 회전
                now_dirs = (now_dirs - 1) % 4
            else:                           # 오른쪽 회전
                now_dirs = (now_dirs + 1) % 4


N = int(input())  # 보드 크기
board = [[0] * N for _ in range(N)]
K = int(input())  # 사과 개수

for _ in range(K):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1  # 사과 표시

L = int(input())  # 방향 변환 횟수
turn = [input().split() for _ in range(L)]  # [X(시간), C(방향, L or D)]
turn_dict = {int(x): c for x, c in turn}
print(simul())

