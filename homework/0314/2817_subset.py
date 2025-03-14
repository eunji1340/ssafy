T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    ct = 0
    
    for i in range(1<<N):
        temp = 0
        for j in range(N):
            if i & (1 << j):
                temp += arr[j]
            if temp > K:
                break
        if temp == K:
            ct += 1
    
    print(f'#{tc} {ct}')