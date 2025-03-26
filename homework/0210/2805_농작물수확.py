def harvest(arr, n):
    result = 0
    middle = n // 2

    for i in range(n):
        if i <= middle:
            for j in range(2*i + 1):
                    result += arr[i][middle-i+j]
        else:
            for j in range(2*(n-i) - 1):
                    result += arr[i][i-middle+j]
    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, [n for n in input()])) for _ in range(N)]
    print(f'#{tc} {harvest(arr, N)}')
