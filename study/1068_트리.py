def count_leaf():
    global ct
    stack = [0]
    visited[0] = 1

    while stack:
        t = stack.pop()
        if t == remove_node:
            continue

        if not tree[t]:
            ct += 1

        for w in tree[t]:
            if not visited[w]:
                stack.append(w)
                visited[w] = 1

N = int(input())  # 노드의 개수
parent = list(map(int, input().split()))  # 각 노드의 부모
remove_node = int(input())  # 지울 노드 번호
visited = [0] * (N+1)
ct = 0
tree = [[] for _ in range(N)]

for i in range(N):
    if parent[i] != -1:
        tree[parent[i]].append(i)

count_leaf()
print(ct)