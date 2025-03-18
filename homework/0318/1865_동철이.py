import sys
sys.stdin = open('input.txt', 'r')

def find_high_prob(col, total):
    global max_prob
    
    if total <= max_prob:
        return
    
    if col == N:
        max_prob = max(max_prob, total)
        return
    
    for row in range(N):
        if not visited[row]:
            visited[row] = 1
            find_high_prob(col + 1, total * (P[row][col] / 100))
            visited[row] = 0  

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]  # 성공 확률
    max_prob = 0
    visited = [0] * N
    find_high_prob(0, 1)
    print(f'#{tc} {max_prob * 100:.6f}')