import sys
import heapq
sys.stdin = open('input.txt', 'r')

def dijkstra(start, end):
    pq = [(0, start)]
    dists = [float('inf')] * (N + 1)
    dists[start] = 0
    
    while pq:
        time, node = heapq.heappop(pq)
        
        if dists[node] < time:
            continue

        for next_time, next_node in edges[node]:
            new_time = time + next_time
            if dists[next_node] > new_time:
                dists[next_node] = new_time
                heapq.heappush(pq, (new_time, next_node))
    
    return dists[end]
            
            
T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())
    edges = [[] for _ in range(N + 1)]
    
    for _ in range(M):
        x, y, c = map(int, input().split())
        edges[x].append([c, y])

    max_time = 0
    for i in range(1, N + 1):
        if i != X:
            max_time = max(max_time, dijkstra(i, X) + dijkstra(X, i))
    print(f'#{tc} {max_time}')
    
#1 10
#2 213
#3 99
#4 253
#5 330
#6 294
#7 305
#8 346
#9 210
#10 50534
