# def fast_typing(A, B):
#     N = len(A)
#     M = len(B)
#
#     cnt = 0
#     i = 0
#     while i <= N - M:
#         for j in range(M):
#             if A[i + j] != B[j]:
#                 break
#         else:
#             cnt += 1
#             i += M
#             continue
#         i += 1
#
#     result = N - (M * cnt) + cnt
#     return result
#
# T = int(input())
# for tc in range(1, T+1):
#     A, B = input().split()
#     print(f'#{tc} {fast_typing(A, B)}')

T = int(input())

for tc in range(1, T+1):
    text, pattern = input().strip().split()

    cnt = 0
    i = 0
    while i <= len(text) - len(pattern):
        if text[i:i+len(pattern)] == pattern:
            cnt += 1
            i += len(pattern)
        else:
            i += 1
    result = len(text) - len(pattern) * cnt - cnt

    print(f'#{tc} {result}')