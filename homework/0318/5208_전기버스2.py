def go(idx, battery, ct):
    global min_ct
    
    battery -= 1
    if ct >= min_ct or battery < 0:
        return
    
    if battery >= 0 and idx == N:
        min_ct = min(min_ct, ct)
        return
    
    go(idx + 1, battery, ct)
    go(idx + 1, M[idx], ct + 1)    

T = int(input())
for tc in range(1, T+1):
    N, *M = map(int, input().split())
    M = [0] + M
    min_ct = 1e9
    go(2, M[1], 0)
    print(f'#{tc} {min_ct}')