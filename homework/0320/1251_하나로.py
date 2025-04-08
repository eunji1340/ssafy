import sys
sys.stdin = open('input.txt', 'r')
import heapq


def prim():
    pq = [(0, 0)]
    visited = [0] * N
    min_cost = ct = 0
    dists = [float('inf')] * N
    dists[0] = 0

    while pq:
        cost, node = heapq.heappop(pq)

        if visited[node]:
            continue

        visited[node] = 1
        min_cost += cost

        ct += 1
        if ct == N:
            return round(min_cost)

        for next_node in range(N):
            if not visited[next_node]:
                new_cost = ((xl[node] - xl[next_node]) ** 2 + (yl[node] - yl[next_node]) ** 2) * E

                if new_cost < dists[next_node]:
                    dists[next_node] = new_cost
                    heapq.heappush(pq, (new_cost, next_node))


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    xl = list(map(int, input().split()))
    yl = list(map(int, input().split()))
    E = float(input())
    print(f'#{tc} {prim()}')

# kruskal
'''
def find_parent(a):
    if parents[a] != a:
        parents[a] = find_parent(parents[a])
    return parents[a]
    

def union(a, b):
    a_root = find_parent(a)
    b_root = find_parent(b)
    
    if a_root != b_root:
        parents[b_root] = a_root
    

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    E = float(input())
    edges = []

    for i in range(N):
        for j in range(i + 1, N):
            cost = E * ((x_list[i] - x_list[j]) ** 2 + (y_list[i] - y_list[j]) ** 2)
            edges.append((cost, i, j))

    edges.sort()

    parents = list(range(N))
    total_cost = ct = 0
    for cost, u, v in edges:
        if find_parent(u) != find_parent(v):
            union(u, v)
            total_cost += cost
            ct += 1
            if ct == N - 1:
                break
                
    print(f'#{tc} {round(total_cost)}')
'''

