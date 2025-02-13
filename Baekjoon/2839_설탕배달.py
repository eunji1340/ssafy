N = int(input())

ct = 0
while N >= 3:
    if N >= 5 and (N % 5) % 3 == 0:
        N -= 5
    elif N >= 3:
        N -= 3
    ct += 1

if N != 0:
    ct = -1

print(ct)