def find_deadlock(arr, n):
    # N = 1, S = 2
    # table : 100 * 100
    ct = 0
    for i in range(n):
        j1, j2 = 0, 0

        while j1 <= n-1:
            for j in range(j1, n):
                if arr[i][j] != '0':
                    j1 = j
            for j in range(j1,n):
                if arr[i][j] != '0':
                    j2 = j

            if arr[i][j1] != arr[i][j2]:
                ct += 1

            j1 = j2

    return ct

for tc in range(1, 11):
    N = int(input())
    table = [list(input().split()) for _ in range(100)]
    print(f'#{tc} {find_deadlock(table, N)}')

