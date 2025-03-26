import sys
sys.stdin = open('input.txt', 'r')

def find_idx(arr):
    count = [0] * 10

    for i in range(6):
        count[arr[i]] += 1
        if count[arr[i]] == 3:
            return i
        for j in range(8):
            if count[j] > 0 and count[j+1] > 0 and count[j+2] > 0:
                return i
        
    return 6  # 못찾은경우

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    p1 = [arr[i] for i in range(len(arr)) if i % 2 == 0]
    p2 = [arr[i] for i in range(len(arr)) if i % 2 == 1]
    
    p1_idx = find_idx(p1)
    p2_idx = find_idx(p2)
    
    if p1_idx < p2_idx:
        result = 1
    elif p1_idx > p2_idx:
        result = 2 
    else:
        result = 0
    
    print(f'#{tc} {result}')
