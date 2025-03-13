def build_top(B):
    global min_height

    for i in range(1 << N):
        height = 0
        for j in range(N):
            if i & (1 << j):
                height += arr[j]
                if height > min_height:
                    break
    
        if B <= height < min_height:
            min_height = height
        
T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())  # 점원 수, 도달해야하는 높이
    arr = list(map(int, input().split()))  # 점원들의 키
    min_height = 1e9
    build_top(B)
    print(f'#{tc} {min_height - B}')