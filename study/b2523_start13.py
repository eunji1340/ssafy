N = int(input())
for i in range(N*2-1):
    if i <= N - 1:
        for j in range(i+1):
            print('*', end='')
    else:
        for j in range(N*2-i-1):
            print('*', end='')
    print()