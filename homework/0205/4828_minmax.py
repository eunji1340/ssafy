T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    Max = arr[0]
    Min = arr[0]

    for num in arr:
        if Max < num:
            Max = num
        if Min > num:
            Min = num

    result = Max - Min
    print(f'#{tc} {result}')