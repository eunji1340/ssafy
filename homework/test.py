def rotate(arr, n):
    # 90도, 180도, 270도 회전 결과 저장할 리스트
    result_90 = [[0] * n for _ in range(n)]
    result_180 = [[0] * n for _ in range(n)]
    result_270 = [[0] * n for _ in range(n)]

    # 회전 과정
    for i in range(n):
        for j in range(n):
            result_90[j][n - i - 1] = arr[i][j]      # 90도 회전
            result_180[n - i - 1][n - j - 1] = arr[i][j]  # 180도 회전
            result_270[n - j - 1][i] = arr[i][j]      # 270도 회전

    # 결과 출력
    for i in range(n):
        print(''.join(map(str, result_90[i])), ''.join(map(str, result_180[i])), ''.join(map(str, result_270[i])))

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc}')
    rotate(arr, N)
