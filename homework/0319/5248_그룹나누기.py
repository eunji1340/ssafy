def find(a):
    global parents
    if parents[a] == a:
        return a
    
    return find(parents[a])

def find2(a):
    global parents
    if parents[a] == a:
        return a
    
    parents[a] = find2(parents[a])
    return parents[a]

def union(a, b):
    aRoot = find(a)
    bRoot = find(b)
    if aRoot != bRoot:
        parents[bRoot] = aRoot
    
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    
    parents = [0] * (N + 1)
    for i in range(1, N + 1):
        parents[i] = i
    
    for i in range(M):
        a = arr[2*i]
        b = arr[2*i + 1]
        
        union(a, b)
    
    groups = set()
    for i in range(1, N + 1):
        groups.add(find(i))
    
    print(f'#{tc} {len(groups)}')