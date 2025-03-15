# def post_order(T):
#     global result
#     if T:
#         post_order(left[T])
#         post_order(right[T])
#         result += key[T]
# 
# T = int(input())
# for tc in range(1, T+1):
#     # 노드의 개수, 리프 노드의 개수, 출력할 노드 번호
#     N, M, L = map(int, input().split())
#     left = [0] * (N+1)
#     right = [0] * (N+1)
#     key = [0] * (N+1)
#     
#     for i in range(M):
#         n, k = map(int, input().split())
#         key[n] = k
# 
#     for i in range(1, N // 2 + 1):
#         left[i] = i * 2
#     for i in range(1, N//2 + N % 2):
#         right[i] = i * 2 + 1
#     
#     result = 0
#     post_order(L)
#     print(f'#{tc} {result}')

import sys
sys.stdin = open('input.txt', 'r')

def build_tree(idx):
    if idx > N:
        return 0
    if tree[idx] != 0:
        return tree[idx]
    
    tree[idx] = build_tree(idx * 2) + build_tree(idx * 2 + 1)
    return tree[idx]
    
T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)
    for _ in range(M):
        idx, num = map(int, input().split())
        tree[idx] = num
    
    build_tree(1)
    print(f'#{tc} {tree[L]}')