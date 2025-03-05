def pre_order(T):
    global ct
    if T:
        ct += 1
        pre_order(left[T])
        pre_order(right[T])
        
T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())  # 간선의 개수, 루트노드
    arr = list(map(int, input().split()))
    left = [0] * (E + 2)
    right = [0] * (E + 2)
    ct = 0

    for i in range(E):
        p, c = arr[i*2], arr[i*2+1]
        
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c

    pre_order(N)
    print(f'#{tc} {ct}')