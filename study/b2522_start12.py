N = int(input())
mid = (2*N-1) // 2
for i in range(2*N-1):
    if i <= mid:
        for j in range(N-i-2, -1, -1):
            print(' ', end='')
        for j in range(i+1):
            print('*', end='')
    else:
        for j in range(i-N+1):
            print(' ', end='')
        for j in range(2*N-i-1):
            print('*', end='')
    print()