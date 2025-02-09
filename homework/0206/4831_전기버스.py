T = int(input())

# def charge_bus(k, n, m, bus_num):
#     ct = 0
#     i = 0
#
#     while i < n:
#         candidates = [c for c in bus_num if (c <= i + k) and (c > i)]
#
#         if i + k >= n:
#             return ct
#
#         if len(candidates) == 0:
#             return 0
#         else:
#             i = max(candidates)
#             ct += 1
#
# for tc in range(1, T+1):
#     K, N, M = map(int, input().split())
#     bus_num = list(map(int, input().split()))
#     print(f'#{tc} {charge_bus(K, N, M, bus_num)}')

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    bus_num = list(map(int, input().split()))
    ct = 0
    i = 0

    while i < N:
        candidates = [c for c in bus_num if (c <= i+K) and (c > i)]

        if i+K >= N:
            break
        if len(candidates) == 0:
            ct = 0
            break
        else:
            i = max(candidates)
            ct += 1

    print(f'#{tc} {ct}')
