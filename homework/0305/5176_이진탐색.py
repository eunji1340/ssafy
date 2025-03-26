# def pre_order(T):
#     global value, num
#     if T:
#         pre_order(left[T])
#         value[T] = num
#         num += 1
#         pre_order(right[T])
# 
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
# 
#     left = [0] * (N + 1)
#     right = [0] * (N + 1)
#     
#     for i in range(1, N//2+1):
#         left[i] = i * 2
#     for i in range(1, N//2 + N % 2):
#         right[i] = i * 2 + 1
#     
#     value = [0] * (N+1)
#     num = 1
#     pre_order(1)
#     
#     print(f'#{tc} {value[1]} {value[int(N/2)]}')

def in_order(i):
    global ct
    if i > N:
        return

    in_order(i * 2)
    tree[i] = ct
    ct += 1
    in_order(i * 2 + 1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1)
    ct = 1
    in_order(1)

    print(f'#{tc} {tree[1]} {tree[N // 2]}')