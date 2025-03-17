def binary_search(num):
    global ans
    l = 0
    r = len(A) - 1
    prev = 0
    check = False
    ct = 0
    
    while l <= r:
        ct += 1
        mid = (l + r) // 2
        if A[mid] == num:
            if check or ct <= 2:
                ans += 1
            return
        
        if num < A[mid]:
            if prev == 1:
                check = True
            prev = -1
            r = mid - 1
        else:
            if prev == -1:
                check = True
            prev = 1
            l = mid + 1
    
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for n in B:
        binary_search(n)
    print(f'#{tc} {ans}')