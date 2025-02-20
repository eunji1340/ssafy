def bfs(S, G):
    visited = [0] * (V+1)
    q = [S]
    visited[S] = 1

    while q:
        t = q.pop(0)
        if t == G:
            return visited[t] - 1

        for w in adj_l[t]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[t] + 1

    return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj_l = [[] for _ in range(V+1)]
    for i in range(E):
        v1, v2 = map(int, input().split())
        adj_l[v1].append(v2)
        adj_l[v2].append(v1)
    S, G = map(int, input().split())

    print(f'#{tc} {bfs(S, G)}')