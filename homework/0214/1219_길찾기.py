def dfs(adj, s):
    visited = [0] * 100
    stack = []

    while True:
        if s == 99:
            return 1

        if visited[s] == 0:
            visited[s] = 1

        for w in adj[s]:
            if visited[w] == 0:
                stack.append(w)
                s = w
                break
        else:
            if stack:
                s = stack.pop()
            else:
                break
    return 0

for tc in range(10):
    n, v = map(int, input().split())
    arr = list(map(int, input().split()))

    adj = [[] for _ in range(100)]
    for i in range(0, len(arr), 2):
        adj[arr[i]].append(arr[i+1])

    print(f'#{n} {dfs(adj, 0)}')