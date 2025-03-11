from collections import deque

N, K = map(int, input().split())
q = deque(range(1, N+1))
arr = []

ct = 0
while q:
    ct += 1
    temp = q.popleft()

    if ct % K == 0:
        arr.append(temp)
    else:
        q.append(temp)

print(f"<{', '.join(str(n) for n in arr)}>")