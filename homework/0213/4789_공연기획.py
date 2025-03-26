T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input()))
    ct = 0
    need_ct = 0

    for i in range(len(arr)):
        if ct < i:
            need_ct += i - ct
            ct += i - ct
        ct += arr[i]

    print(f'#{tc} {need_ct}')