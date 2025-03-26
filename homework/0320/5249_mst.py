import sys
sys.stdin = open('input.txt', 'r')

def find_parent(x):
    if parents[x] == x:
        return x
    parents[x] = find_parent(parents[x])
    return parents[x]


def union(x, y):
    x_root = find_parent(x)
    y_root = find_parent(y)
    
    if x_root == y_root:
        return
    
    parents[y_root] = x_root


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    
    edges = []
    
    for _ in range(E):
        start, end, w = map(int, input().split())
        edges.append((start, end, w))
        
    edges.sort(key=lambda x: x[2])
    parents = [i for i in range(V + 1)]
    
    result = 0
    ct = 0

    for s, e, w in edges:
        if find_parent(s) != find_parent(e):
            union(s, e)
            result += w
            ct += 1
            
            if ct == V:
                break

    print(f'#{tc} {result}')