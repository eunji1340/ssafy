def binary_serch(n):
    global ans
    l = 0
    r = N - 1
    prev = 0
    check = True
    
    while l <= r:
        m = (l + r) // 2
        
        if A[m] == n:
            if check:
                ans += 1
            return
        
        if n < A[m]:
            r = m - 1
            now = -1
        else:
            l = m + 1
            now = 1
            
        if prev == now:
            check = False
        prev = now
    return

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))
    ans = 0
    
    for num in B:
        binary_serch(num)
    
    print(f'#{tc} {ans}')