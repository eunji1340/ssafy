T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())    # 상자의 개수, 작업 횟수
    # change[0] = L번, change[1] = R번
    change = [list(map(int, input().split())) for _ in range(Q)]
    box = [0] * N

    for i in range(Q):
        for j in range(change[i][0], change[i][1] + 1):
            box[j-1] = i + 1

    print(f'#{tc} {" ".join(map(str, box))}')