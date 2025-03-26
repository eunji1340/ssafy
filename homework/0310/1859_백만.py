import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    profit = 0
    max_num = arr[N-1]
    
    for i in range(N-2, -1, -1):
        if arr[i] < max_num:
            profit += max_num - arr[i]
            
        max_num = max(max_num, arr[i])
        
    print(f'#{tc} {profit}')