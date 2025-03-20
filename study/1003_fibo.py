def fib(n):
    global ct1, ct2
    if n == 0:
        ct1 += 1
        return 0
    elif n == 1:
        ct2 += 1
        return 1

    if dp[n] != -1:
        return dp[n]

    dp[n] = fib(n - 1) + fib(n - 2)
    return dp[n]



T = int(input())
for tc in range(T):
    N = int(input())
    ct1 = ct2 = 0
    dp = [-1] * (N + 2)
    dp[0], dp[1] = 0, 1
    fib(N)
    print(f'{ct1} {ct2}')