from sys import stdin
def input():
    return stdin.readline().rstrip()

M, N = map(int, input().split())
for i in range(M, N + 1):
    if i == 1:
        continue
    for j in range(2, int(i ** (1/2)) + 1):
        if i % j == 0:
            break
    else:
        print(i)


'''
def check_num(num):
    if num > N:
        return

    if num == 1:
        num += 1

    for i in range(2, int(num**(1/2)) + 1):
        if num % i == 0:
            break
    else:
        print(num)

    check_num(num + 1)

M, N = map(int, input().split())
check_num(M)
'''