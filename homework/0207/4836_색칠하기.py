T = int(input())
for tc in range(1, T+1):
    N = int(input())
    space = [list(map(int, input().split())) for _ in range(N)]
    ct = 0
    tile = [[0] * 10 for _ in range(10)]

    for s in space:
        r1, c1, r2, c2, color = map(int, s)
        for r in range(10):
            for c in range(10):
                if (r1 <= r <= r2) and (c1 <= c <= c2):
                    tile[r][c] += color

                if tile[r][c] == 3:
                    ct += 1

    print(f'#{tc} {ct}')

# 내 꺼
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     tile = [[0] * 10 for _ in range(10)]
#     ct = 0
#
#     for num in range(N):
#         space = arr[num]
#         for i in range(10):
#             for j in range(10):
#                 if space[0] <= i <= space[2] and space[1] <= j <= space[3]:
#                     if tile[i][j] == 0:
#                         tile[i][j] = space[-1]
#                     elif tile[i][j] == space[-1]:
#                         continue
#                     else:
#                         ct += 1
#
#     print(f'#{tc} {ct}')

# 강사님 코드
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [[0]*10 for _ in range(10)]
#
#     for _ in range(N):
#         r1, c1, r2, c2, color = list(map(int, input().split()))
#
#         for r in range(r1, r2 + 1):
#             for c in range(c1, c2 + 1):
#                 arr[r][c] += color
#
#         area = 0
#         for r in range(10):
#             for c in range(10):
#                 if arr[r][c] == 3:
#                     area += 1
#
#         print(f"#{tc} {area}")
