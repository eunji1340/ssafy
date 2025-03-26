import sys
#sys.stdin = open('input.txt', 'r')

import heapq


def dijstra(start):
    pq = [(0, start)]
    dists = [float('inf')] * (N + 1)
    dists[start] = 0
    
    while pq:
        dist, node = heapq.heappop(pq)
        
        if dists[node] < dist:
            continue
        
        for next_node, next_dist in graph[node]:  
            new_dist = dist + next_dist
            
            if dists[next_node] > new_dist:
                dists[next_node] = new_dist
                heapq.heappush(pq, (new_dist, next_node))
                
    return dists[N]
    
    
T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
    
    print(f'#{tc} {dijstra(0)}')