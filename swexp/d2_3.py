T = int(input())
N = [int(input()) for i in range(T)]
for i in range(T):
    result = 0
    print(f'#{i+1}', end=' ')

    for j in range(N[i]+1):
        if j%2==1:
            result += j
        else:
            result -= j
    print(result)