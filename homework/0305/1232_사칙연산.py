def pre_order(T):
    if T:       
        pre_order(left[T])
        pre_order(right[T])
        
        temp = tree[T]
        if temp == '+':
            tree[T] = tree[left[T]] + tree[right[T]]
        elif temp == '-':
            tree[T] = tree[left[T]] - tree[right[T]]
        elif temp == '*':
            tree[T] = tree[left[T]] * tree[right[T]]
        elif temp == '/':
            tree[T] = tree[left[T]] // tree[right[T]]

        if T == 1:
            return tree[T]

for tc in range(1, 11):
    N = int(input())  # 정점의 개수
    left = [0] * (N+1)
    right = [0] * (N+1)
    tree = [''] * (N+1)
    
    for _ in range(N):
        arr = input().split()
        p = int(arr[0])
        if len(arr) == 4:
            left[p] = int(arr[2])
            right[p] = int(arr[3])
            tree[p] = arr[1]
        else:
            tree[p] = int(arr[1])
    
    print(f'#{tc} {pre_order(1)}')
