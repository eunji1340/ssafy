N = int(input())  # 트리의 정점 개수
tree = [[] for _ in range(N+1)]
bridge = [[] for _ in range(N-1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
    bridge.append()
print(tree)
q = int(input())
for _ in range(q):
    t, k = map(int, input().split())
    if t == 1:
        if len(tree[k]) > 1:
            print('yes')
        else:
            print('no')
    elif t == 2:
