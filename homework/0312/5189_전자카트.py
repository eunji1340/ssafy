def find_min_energy():
    global min_energy
    energy = 0
    visited = [0] * (N + 1)
    
    if 
    
    

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_energy = 1e9
    find_min_energy()
    print(f'#{tc} {min_energy}')