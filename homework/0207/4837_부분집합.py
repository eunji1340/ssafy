T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(range(1, 13))
    result = 0

    for i in range(1 << 12):
        temp = []
        for j in range(12):
            if i & (1 << j):
                temp.append(arr[j])
        if len(temp) == N and sum(temp) == K:
                result += 1

    print(f'#{tc} {result}')


# 강사님 코드
# A = list(range(1,13))
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     cnt = 0
#     for i in range(1 << 12):
#         one_cnt = 0
#         val_sum = 0
#
#         for j in range(12):
#             if i & (1 << j):
#                 one_cnt += 1
#                 val_sum += A[j]
#
#         if one_cnt == N and val_sum == K:
#             cnt += 1

