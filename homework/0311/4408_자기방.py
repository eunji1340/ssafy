import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    path = [0] * 401

    for _ in range(N):
        s, e = map(int, input().split())
        if s > e:
            s, e = e, s
        
        start = (s + 1) // 2
        end = (e + 1) // 2
        for i in range(start, end+1):
            path[i] += 1
    
    time = max(path)
    
    print(f'#{tc} {time}')