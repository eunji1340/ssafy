from collections import deque
import sys

input = sys.stdin.readline  # 빠른 입력을 위해 추가

def find_parent(s):
    visited = [0] * (N+1)
    q = deque([s])
    visited[s] = 1

    while q:
        t = q.popleft()
        for w in tree[t]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = t

    return visited

N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

parents = find_parent(1)
for parent in parents[2:]:
    print(parent)