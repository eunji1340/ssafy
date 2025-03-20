import sys
sys.stdin = open('graph.txt', 'r')


def prim(start_node):
    pq = [(0, start_node)]
    MST = [0] * V
    min_weight = 0

    while pq:
        weight, node = heapq.heappop(pq)

        if MST[node]:
            continue

        MST[node] = 1
        min_weight += weight

        for next_node in range(V):
            if graph[node][next_node] == 0:
                continue
            if MST[next_node]:
                continue
            heapq.heappush(pq, (graph[node][next_node], next_node))

    return min_weight

import heapq
V, E = map(int, input().split())
graph = [[0] * V for _ in range(V)]

for _ in range(E):
    start, end, weight = map(int, input().split())
    graph[start][end] = weight
    graph[end][start] = weight

result = prim(0)
print(f'{result}')