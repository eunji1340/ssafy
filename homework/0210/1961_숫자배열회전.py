# def rotate(arr, n):
#     result_90 = [[0] * n for _ in range(n)]
#     result_180 = [[0] * n for _ in range(n)]
#     result_270 = [[0] * n for _ in range(n)]
#
#     for i in range(n):
#         for j in range(n):
#             result_90[j][n - i - 1] = str(arr[i][j])      # 90도 회전
#             result_180[n - i - 1][n - j - 1] = str(arr[i][j])  # 180도 회전
#             result_270[n - j - 1][i] = str(arr[i][j])      # 270도 회전
#
#     for i in range(n):
#         print(''.join(result_90[i]), ''.join(result_180[i]), ''.join(result_270[i]))
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     print(f'#{tc}')
#     rotate(arr, N)

# 강사님 코드
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    ans = [""] * N

    for c in range(N):
        for r in range(N-1, -1, -1):
            ans[c] += arr[r][c]
        ans[c] += " "

    for r in range(N-1, -1, -1):
        for c in range(N-1, -1, -1):
            ans[N - 1 - r] += arr[r][c]
        ans[N - 1 - r] += " "

    for c in range(N-1, -1, -1):
        for r in range(N):
            ans[N - 1 - c] += arr[r][c]


    print(f"{tc}")
    for line in ans:
        print(line)


