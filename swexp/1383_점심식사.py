def move(time):
    
    if time 
    
    
    

    


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    stairs = []
    peoples = []
    min_time = float('inf')

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                peoples.append([i, j])
            elif arr[i][j] > 1:
                stairs.append([i, j, arr[i][j]])


    print(f'#{tc}')