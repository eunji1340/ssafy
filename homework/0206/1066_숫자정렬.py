T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    count = [0] * (max(arr)+1)
    sort_arr = [0] * N

    # 카운트
    for i in range(N):
        count[arr[i]] += 1

    # 누적합
    for i in range(1, max(arr)+1):
        count[i] += count[i-1]

    for i in range(N-1, -1, -1):
        count[arr[i]] -= 1
        sort_arr[count[arr[i]]] = arr[i]

    print(f'#{tc} {" ".join(map(str, sort_arr))}')

    # for i in range(N-1, 0, -1):
    #     for j in range(i):
    #         if arr[j] > arr[j+1]:
    #             arr[j], arr[j+1] = arr[j+1], arr[j]
    #
    # print(f'#{tc} {" ".join(map(str, arr))}')
