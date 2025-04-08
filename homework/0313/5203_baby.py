import sys
#sys.stdin = open('input.txt', 'r')

def baby_gin(cards):
    count = [0] * 10
    for i in range(6):
        count[cards[i]] += 1
        if count[cards[i]] == 3:
            return i
        for j in range(8):
            if count[j] and count[j + 1] and count[j + 2]:
                return i
    return 10

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    p1 = [arr[i] for i in range(len(arr)) if i % 2 == 0]
    p2 = [arr[i] for i in range(len(arr)) if i % 2 == 1]
    
    p1_idx = baby_gin(p1)
    p2_idx = baby_gin(p2)

    if p1_idx == p2_idx == 10:
        result = 0
    elif p1_idx <= p2_idx:
        result = 1
    else:
        result = 2
    
    print(f'#{tc} {result}')
