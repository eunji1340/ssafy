def is_valid(i):
    global ans

    if i > N:
        return False

    left = is_valid(i * 2)
    right = is_valid(i * 2 + 1)

    if tree[i] in '+-*/':
        if not left and right:
            ans = 0
        return True
    else:
        if left or right:
            ans = 0
        return True

for tc in range(1, 11):
    N = int(input())
    tree = [''] * (N+1)
    for _ in range(N):
        idx, key, *c = input().split()
        tree[int(idx)] = key

    ans = 1
    is_valid(1)
    print(f'#{tc} {ans}')
