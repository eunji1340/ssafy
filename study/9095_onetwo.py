def recur(num):
    global ct
    if num > N:
        return
    if num == N:
        ct += 1
        return
    recur(num + 1)
    recur(num + 2)
    recur(num + 3)

T = int(input())
for tc in range(T):
    N = int(input())
    ct = 0
    recur(0)
    print(ct)