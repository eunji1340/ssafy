def binary_serch(P, A, B):
    def search(P, key):
        start = 1
        end = P
        ct = 0

        while start <= end:
            ct += 1
            middle = (start+end)//2
            if key == middle:
                break
            elif key > middle:
                start = middle + 1
            else:
                end = middle - 1
        return ct

    if search(P, A) < search(P, B):
        return 'A'
    elif search(P, A) > search(P, B):
        return 'B'
    else:
        return 0

T = int(input())

for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    print(f'#{tc} {binary_serch(P, A, B)}')

# # 강사님 코드
# T = int(input())
# def binary_serch_cnt(N, target):
#     l = 1
#     r = N
#     cnt = 0
#
#     while l < r:
#         c = (l + r) // 2
#         cnt += 1
#
#         if c == target:
#             return cnt
#         elif c > target:
#             r = c - 1
#         else:
#             l = c + 1
#
# for tc in range(1, T+1):
#     P, A, B = list(map(int, input().split()))
#     A_cnt = binary_serch_cnt(P, A)
#     B_cnt = binary_serch_cnt(P, B)
#
#     ans = '0'
#     if A_cnt < B_cnt:
#         ans = 'A'
#     elif A_cnt > B_cnt:
#         ans = 'B'
#
#     print(f'#{tc} {ans}')