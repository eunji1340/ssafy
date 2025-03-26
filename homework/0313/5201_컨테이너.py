T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    result = 0
    w.sort(reverse=True)
    trucks.sort(reverse=True)
    
    w_idx = 0
    for t in trucks:
        while w_idx < N and t < w[w_idx]:
            w_idx += 1

        result += w[w_idx]
        w_idx += 1
        if w_idx == N:
            break
    
    print(f'#{tc} {result}')