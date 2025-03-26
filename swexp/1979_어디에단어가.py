# def find_position(arr, n, k):
#     ct = 0
#
#     # 가로
#     for i in range(n):
#         for j in range(n-k+1):
#             if sum(arr[i][j:j+k]) == k and (j == 0 or arr[i][j-1] == 0):
#                 if j+k == n or arr[i][j+k] == 0:
#                     ct += 1
#
#     # 세로
#     for j in range(n):
#         for i in range(n-k+1):
#             if sum(arr[row][j] for row in range(i, i + k)) == k and (i == 0 or arr[i-1][j] == 0):
#                 if i+k == n or arr[i+k][j] == 0:
#                     ct += 1
#
#     return ct
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     puzzle = [list(map(int, input().split())) for _ in range(N)]
#     print(f'#{tc} {find_position(puzzle, N, K)}')

T = int(input())
for tc in range(1, T+1):
    N, K = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0

    for r in range(N):
        cnt = 0
        for c in range(N):
            if arr[r][c] == 1:
                cnt += 1
                if cnt == K:
                    ans += 1
                    if c+1 < N and arr[r][c+1] == 1:
                        ans -= 1
            else:
                cnt = 0

    for c in range(N):
        cnt = 0
        for r in range(N):
            if arr[r][c] == 1:
                cnt += 1
                if cnt == K:
                    ans += 1
                    if r+1 < N and arr[r+1][c] == 1:
                        ans -= 1
            else:
                cnt = 0

    print(f'#{tc} {ans}')