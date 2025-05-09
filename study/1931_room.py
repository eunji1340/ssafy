N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: (x[1], x[0]))

prev_e = ct = 0
for s, e in arr:
    if s >= prev_e:
        ct += 1
        prev_e = e

print(ct)