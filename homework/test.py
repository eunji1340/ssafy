'''
7 8
4 2 1 2 1 3 5 2 4 6 5 6 6 7 3 7
'''

def bfs(s, V):
    visited = [0] * (V + 1)
    q = []
    q.append(s)
    visited[s] = 1
    while q:
        t = q.pop(0)
        print(t)
        for w in adj_l[t]:
            if visited[w] == 0:
                q.append(w)
                visited[w]


V, E = map(int, input().split())  # 1번부터 V번 정점, E개의 간선
arr = list(map(int, input().split()))

# 인접리스트
adj_l = [[] for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)

bfs(1, 7)