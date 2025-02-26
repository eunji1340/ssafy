string = input()
N = len(string)

R = 0
for i in range(1, N+1):
    if N % i == 0 and R < i and i <= N // i:
        R = i
C = N // R

arr = [['']*C for _ in range(R)]

i = 0
for c in range(C):
    for r in range(R):
        arr[r][c] = string[i]
        i += 1

for a in arr:
    print(''.join(a), end='')