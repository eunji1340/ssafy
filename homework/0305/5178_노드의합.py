def post_order(T):
    global result
    if T:
        post_order(left[T])
        post_order(right[T])
        result += key[T]

T = int(input())
for tc in range(1, T+1):
    # 노드의 개수, 리프 노드의 개수, 출력할 노드 번호
    N, M, L = map(int, input().split())
    left = [0] * (N+1)
    right = [0] * (N+1)
    key = [0] * (N+1)
    
    for i in range(M):
        n, k = map(int, input().split())
        key[n] = k

    for i in range(1, N // 2 + 1):
        left[i] = i * 2
    for i in range(1, N//2 + N % 2):
        right[i] = i * 2 + 1
    
    result = 0
    post_order(L)
    print(f'#{tc} {result}')