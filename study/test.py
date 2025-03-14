import sys

#sys.stdin = open('input.txt', 'r')

# 대각선 방향 이동 (우하 → 좌하 → 좌상 → 우상)
directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]


def dfs(sr, sc, r, c, visited, direction, count):
    global max_ct

    # 사각형을 만들면서 출발점으로 돌아온 경우
    if direction == 3 and (r, c) == (sr, sc) and count > 3:
        max_ct = max(max_ct, count)
        return

    # 다음 이동
    for i in range(direction, 4):  # 현재 방향 유지 or 한 단계 회전 가능
        nr, nc = r + directions[i][0], c + directions[i][1]

        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] not in visited:
            visited.add(arr[nr][nc])
            dfs(sr, sc, nr, nc, visited, i, count + 1)
            visited.remove(arr[nr][nc])  # 백트래킹


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_ct = -1  # 최소한 한 번은 사각형을 만들어야 하므로 -1로 설정

    for r in range(0, N - 1):  # 경계 줄이기 (1, N-2)도 가능
        for c in range(1, N - 1):
            dfs(r, c, r, c, set([arr[r][c]]), 0, 1)

    print(f'#{tc} {max_ct}')
