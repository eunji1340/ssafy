import copy
from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())  # 세로, 가로
lab = [list(map(int, input().split())) for _ in range(N)]  # 지도
empty = []  # 빈 칸 위치 -> 벽 세울 수 있음
virus = []  # 바이러스 위치

for r in range(N):
    for c in range(M):
        if lab[r][c] == 0:  # 벽이면
            empty.append((r, c))
        elif lab[r][c] == 2:  # 바이러스면
            virus.append((r, c))


# 벽 세울 위치 조합
def combinations():
    result = []
    length = len(empty)
    for i in range(length):
        for j in range(i + 1, length):
            for k in range(j + 1, length):
                result.append([empty[i], empty[j], empty[k]])  # 위치 3개 뽑아서 넣기
    return result


# 바이러스 뿌려
def spread_virus(copy_lab):
    q = deque(virus)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while q:
        r, c = q.popleft()

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and copy_lab[nr][nc] == 0:  # 빈 칸이면 다 바이러스야
                copy_lab[nr][nc] = 2
                q.append((nr, nc))  # 다음으로 이동


# 안전 구역 세기
def count_safe_area(copy_lab):
    count = 0
    for i in range(N):
        for j in range(M):
            if copy_lab[i][j] == 0:  # 0인 곳 -> 안전
                count += 1
    return count


max_safe_area = 0  # 최종 출력 값, 최대 안전 구역
wall_comb = combinations()  # 벽 조합 구하기

for walls in wall_comb:  # 조합들 속에서 하나 씩 빼와
    copy_lab = copy.deepcopy(lab)  # 원본 바꾸면 안되니깐 카피

    for r, c in walls:  # 벽들의 위치 빼오기
        copy_lab[r][c] = 1  # 벽 세워버리기

    spread_virus(copy_lab)  # 바이러스 뿌려버리기
    safe = count_safe_area(copy_lab)  # 안전구역 세버리기
    max_safe_area = max(max_safe_area, safe)  # 최대 구역 구해버려

print(max_safe_area)  # 출력해
