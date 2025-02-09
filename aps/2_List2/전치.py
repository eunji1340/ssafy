# arr = [[1,2,3],[4,5,6],[7,8,9]]
#
# for i in range(3):
#     for j in range(3):
#         if i<j:
#             arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
#
# print(arr)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    total = 0

    for i in range(N):
        for j in range(N):
            for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
                ni = i + di
                nj = j + dj
                if 0<=ni<N and 0<=nj<N:
                    total += abs(arr[ni][nj] - arr[i][j])
    print(total)