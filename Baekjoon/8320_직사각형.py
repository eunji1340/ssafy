n = int(input())

rec = [0] * (n + 1)
rec[0] = 0
rec[1] = 1

for i in range(2, n+1):
    ct = 0
    for width in range(1, int(i ** 0.5) + 1):
        if i % width == 0:
            ct += 1
    rec[i] = rec[i-1] + ct

print(rec[n])
