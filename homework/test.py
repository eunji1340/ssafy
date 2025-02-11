T = int(input())

def binary_search(P, key):
    start = 1
    end = P
    ct = 0

    while start <= end:
        middle = (start+end) // 2
        ct += 1

        if key == middle:
            return ct
        elif key > middle:
            start = middle + 1
        else:
            end = middle - 1
    return ct

for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    A_ct = binary_search(P, A)
    B_ct = binary_search(P, B)

    result = '0'
    if A_ct < B_ct:
        result = 'A'
    elif A_ct > B_ct:
        result = 'B'

    print(f'#{tc} {result}')