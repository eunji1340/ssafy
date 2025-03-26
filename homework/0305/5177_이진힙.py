def enq(n):
    global last
    last += 1
    heap[last] = n
    
    c = last
    p = c // 2
    while p and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c//2
        
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    heap = [0] * (N + 1)
    last = 0
    for a in arr:
        enq(a)
    
    result = 0
    
    while last != 0:
        result += heap[last // 2]
        last //= 2
        
    print(f'#{tc} {result}')
    
    
'''
def enq(num, c_idx):
    heap[c_idx] = num
    
    p_idx = c_idx // 2
    while heap[p_idx] > heap[c_idx] and p_idx > 0:
        heap[p_idx], heap[c_idx] = heap[c_idx], heap[p_idx]
        c_idx //= 2
        p_idx = c_idx // 2

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    
    heap = [0] * (N+1)
    
    for idx, num in enumerate(nums, start=1):
        enq(num, idx)

    result = 0
    while N > 0:
        result += heap[N // 2]
        N //= 2
    
    print(f'#{tc} {result}')
'''