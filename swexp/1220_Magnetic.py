def find_deadlock(arr, n):
    # N = 1, S = 2
    # table : 100 * 100
    ct = 0

    for c in range(100):
        prev = 0
        for r in range(100):
            if arr[r][c] == '1':
                prev = 1
            elif arr[r][c] == '2' and prev == 1:
                ct += 1
                prev = 0

    return ct

for tc in range(1, 11):
    N = int(input())
    table = [list(input().split()) for _ in range(100)]
    print(f'#{tc} {find_deadlock(table, N)}')

