# def in_order(T):
#     global result
#     if T:
#         in_order(left[T])
#         result += key[T]
#         in_order(right[T])
# 
# for tc in range(1, 11):
#     N = int(input())
#     left = [0 for _ in range(N+1)]
#     right = [0 for _ in range(N+1)]
#     key = ['' for _ in range(N+1)]
#     
#     for i in range(N):
#         arr = input().split()
#         p = int(arr[0])
#         k = arr[1]
#         cl = cr = 0
#         
#         if len(arr) >= 3:
#             cl = int(arr[2])
#         if len(arr) == 4:
#             cr = int(arr[3])
#         
#         left[p] = cl
#         right[p] = cr
#         key[p] = k
#     
#     result = ''
#     in_order(1)
#     print(f'#{tc} {result}')

import sys
sys.stdin = open('input.txt', 'r')

def in_order(i):
    global result
    if i <= N:
        in_order(i * 2)
        result += tree[i]
        in_order(i * 2 + 1)

for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N+1)
    result = ''
    
    for _ in range(N):
        idx, key, *c = input().split()
        tree[int(idx)] = key
    
    in_order(1)
    print(f'#{tc} {result}')