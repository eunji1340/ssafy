import sys
sys.stdin = open('input.txt', 'r')

def find_max_money(arr, ct, visited):
    global max_money
    money = int(''.join(str(n) for n in arr))
    
    if (tuple(arr), ct) in visited:
        return
    
    visited.add((tuple(arr), ct))
    
    if ct == 0:
        max_money = max(max_money, money)
        return
    
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]
            find_max_money(arr, ct - 1, visited)
            arr[i], arr[j] = arr[j], arr[i]
            
T = int(input())
for tc in range(1, T+1):
    arr, ct = input().split()
    ct = int(ct)
    arr = list(map(int, arr))
    max_money = 0
    visited = set()
    find_max_money(arr, ct, visited)
    print(f'#{tc} {max_money}')