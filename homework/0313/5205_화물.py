T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    arr.sort(key=lambda x: x[1])
    
    prev_e = 0
    count = 0
    for s, e in arr:
        if s >= prev_e:
            count += 1
            prev_e = e
    
    print(f'#{tc} {count}')
