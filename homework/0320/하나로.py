import sys
sys.stdin = open('input.txt', 'r')

import heapq


def prim():
    pq = [(0, 0)]
    mst = [0] * N
    min_cost = ct = 0
    
    while pq:
        cost, node = heapq.heappop(pq)
        
        if mst[node]:
            continue
            
        mst[node] = 1
        min_cost += cost
        ct += 1
        
        if ct == N:
            return min_cost
        
        for next_node in range(N):
            if mst[next_node]:
                continue
            cost = ((x_list[node] - x_list[next_node]) ** 2 + (y_list[node] - y_list[next_node]) ** 2) * E
            heapq.heappush(pq, (cost, next_node))


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    E = float(input())

    print(f'#{tc} {round(prim())}')

'''
1
4
0 0 400 400
0 100 0 100
1.0
'''