def find_min_energy(arr):
    global min_energy
    
    for p in arr:
        energy = e[0][p[0]-1]
        for i in range(len(p)-1):
            energy += e[p[i]-1][p[i+1]-1]
        energy += e[p[-1] - 1][0]
        min_energy = min(min_energy, energy)
    
def find_path(cnt):
    if cnt == N-1:
        path_arr.append(path[:])
        return
    
    for num in range(2, N+1):
        if used[num] is True:
            continue

        used[num] = True
        path.append(num)
        find_path(cnt + 1)
        path.pop()
        used[num] = False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    e = [list(map(int, input().split())) for _ in range(N)]
    used = [False] * (N + 1)
    path = [1]
    path_arr = []
    used[1] = True
    
    find_path(1)
    min_energy = 1e9
    find_min_energy(path_arr)
     
    print(f'#{tc} {min_energy}')