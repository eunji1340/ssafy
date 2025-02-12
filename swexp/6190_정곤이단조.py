T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    mul = []
    result = -1

    for i in range(N-1):
        for j in range(i+1, N):
            mul.append(arr[i] * arr[j])

    mul.sort(reverse=True)

    for n in mul:
        temp = n
        num_str = str(n)
        for i in range(len(str(n)) - 1):
            if num_str[i] > num_str[i+1]:
                break
        else:
            result = temp
            break

    print(f'#{tc} {result}')