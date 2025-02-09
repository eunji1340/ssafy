# N = 2
# M = 3
# for i in range(N):
#     for j in range(M):
#         for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
#             ni = i + di
#             nj = j + dj
#             if 0<=ni<N and 0<=nj<M:
#                 print(ni, nj, i, j)

max_v = 0
for i in range(N):
    for j in range(N):
        s = arr[i][j]
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            for c in range(1, k+1)
                ni, nj = i+di*c, j+dj*c
                if 0 <= ni < N and 0 <= nj < N:
                    s += arr[ni][nj]

            if max_v < s:
                max_v = s