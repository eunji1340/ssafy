import heapq


def dijkstra(start_node):
    pq = [(0, start_node)]
    dists = [INF] * V
    dists[start_node] = 0

    while pq:
        dist, node = heapq.heappop(pq)

        if dists[node] < dist:
            continue

        for next_info in graph[node]:
            next_dist = next_info[0]
            next_node = next_info[1]

            new_dist = dist + next_dist

            if new_dist >= dists[next_node]:
                continue

            dists[next_node] = new_dist
            heapq.heappush(pq, (new_dist, next_node))

    return dists


INF = int(21e8)

V, E = map(int, input().split())
start_node = 0
graph = [[] for _ in range(V)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

result_dists = dijkstra(0)
print(result_dists)