# 간단한 소인수분해

T = int(input())
N = [int(input()) for i in range(T)]

for i in range(T):
    n = N[i]
    print(f'#{i+1}', end=' ')
    for j in [2,3,5,7,11]:
        ex = 0
        while(n%j==0):
            ex += 1
            n /= j
        print(ex, end=' ')
    print()