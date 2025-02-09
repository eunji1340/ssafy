# T = int(input())
#
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     A = [num for num in range(1,13)]
#     ct = 0
#     subset = []
#     for i in range(1 << 12):
#         temp = []
#         for j in range(12):
#             if i & (1 << j):
#                 temp.append(A[j])
#         if len(temp) == N:
#             subset.append(temp)
#
#     for i in subset:
#         if sum(i) == K:
#             ct += 1
#
#     print(f'#{tc} {ct}')

T = int(input())

A = list(range(1, 13))

for tc in range(1, T+1):
    N, K = list(map(int, input().split()))
    cnt = 0
    for i in range(1 << 12):
        one_cnt = 0
        val_sum = 0
