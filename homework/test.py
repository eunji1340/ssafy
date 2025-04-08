import heapq

def prim():
    pq = [(0, 0)]
    visited = [0] * (N + 1)
    costs = [float('inf')] * (N + 1)
    costs[0] = 0
    min_cost = ct = 0
    
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
            if visited[next_node]:
                continue
            next_cost = ((xl[node] - xl[next_node]) ** 2 + (yl[node] - yl[next_node]) ** 2) * E
            if next_cost < costs[next_node]:
                costs[next_node] = next_cost
                heapq.heappush(pq, (next_cost, next_node))
        

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    xl = list(map(int, input().split()))
    yl = list(map(int, input().split()))
    E = float(input())
    print(f'#{tc} {prim()}')