def bfs(adj, S, G):
    q = [S]
    visited = [0] * (V + 1)
    visited[S] = 1

    while q:
        i = q.pop(0)
        if i == G:
            return visited[i] - 1

        for ni in adj[i]:
            if visited[ni] == 0:
                q.append(ni)
                visited[ni] = visited[i] + 1

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())

    adj = [[] for _ in range(V + 1)]
    for i in range(E):
        v1, v2 = map(int, input().split())
        adj[v1].append(v2)
        adj[v2].append(v1)
    S, G = map(int, input().split())
    print(f'#{tc} {bfs(adj, S, G)}')