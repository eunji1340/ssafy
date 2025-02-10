def ladder(arr):
    for col in range(100):
        if arr[99][col] == 2:
            c = col
            break

    r = 99
    while r > 0:
        if c > 0 and arr[r][c-1] == 1:
            while c > 0 and arr[r][c-1] == 1:
                c -= 1
        elif c < 99 and arr[r][c+1] == 1:
            while c < 99 and arr[r][c+1] == 1:
                c += 1
        r -= 1

    return c

for tc in range(10):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    print(f'#{N} {ladder(arr)}')
