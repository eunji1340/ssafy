def find(a):
    if parents[a] == a:
        return a
    
    return find(parents[a])
    

def union(a, b):
    a_root = find2(a)
    b_root = find2(b)
    if a_root != b_root:
        parents[b] = a_root


def find2(a):
    global parents
    if parents[a] == a:
        return a

    parents[a] = find2(parents[a])
    return parents[a]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    
    parents = [0] * (N + 1)
    for i in range(1, N + 1):
        parents[i] = i
        
    for i in range(M):
        a = arr[i * 2]
        b = arr[i * 2 + 1]
        union(a, b)
    print(parents)
