def select(idx, selected):
    if len(selected) == N // 2:
        food_lst.append(selected[:])
        return
    
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = 1
            selected.append(i)
            select(i + 1, selected)
            selected.pop()
            visited[i] = 0


def cook(A, B):
    global min_dif
    s1, s2 = 0, 0
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            s1 += synergy[A[i]][A[j]] + synergy[A[j]][A[i]]
            s2 += synergy[B[i]][B[j]] + synergy[B[j]][B[i]]

    min_dif = min(min_dif, abs(s1 - s2))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    synergy = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    min_dif = 1e9
    food_lst = []
    select(0, [])

    for food in food_lst:
        B = [i for i in range(N) if i not in food]  # A에 없는 나머지 재료들
        cook(food, B)

    print(f'#{tc} {min_dif}')
    
'''

1
4
0 5 3 8
4 0 4 1
2 5 0 3
7 2 3 0
'''