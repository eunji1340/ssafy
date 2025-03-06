def bfs(i):
    front, rear = -1, 0
    visited = [0] * (N + 1)
    q = [0] * N
    q[rear] = i
    visited[i] = 1              
    while front < rear:
        front += 1
        r = q[front]
        for j in adj_matrix[r]:
            if j == 0:
                continue
            if not visited[j]:
                visited[j] = visited[r] + 1
                rear += 1
                q[rear] = j                 
    S = sum(visited)
    return S

N, E = map(int, input().split())
edge = list(list(map(int, input().split())) for _ in range(E))

adj_matrix = [[0] * (N + 1) for _ in range(N + 1)]
S = [0] * (N + 1)

for s, e in edge:
    adj_matrix[s][e] = e
    adj_matrix[e][s] = s

for i in range(1, N + 1):
    S[i] = bfs(i)

m = min(S[1:])
for i in range(1, N + 1):
    if S[i] == m:
        break
print(i)