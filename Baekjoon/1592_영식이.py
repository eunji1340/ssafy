N, M, L = map(int, input().split())
dict = {}

for i in range(1, N+1):
    dict[i] = 0

pass_idx = 1
ct = 0

while max(dict.values()) < M:
    dict[pass_idx] += 1
    if dict[pass_idx] % 2 != 0:
        pass_idx = (pass_idx + L) % N if (pass_idx + L) != N else N
    else:
        pass_idx = (pass_idx - L) % N if (pass_idx - L) != 0 else N
    ct += 1

print(ct-1)