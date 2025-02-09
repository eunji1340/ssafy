def find_max(A, B):
    if len(B) < len(A):
        A, B = B, A
    max = 0
    for _ in range(len(B) - len(A) + 1):
        temp = sum(list(map(lambda a, b : a * b, A, B)))
        if temp > max:
            max = temp
        B.pop(0)
    return max

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(f'#{test_case}', end = ' ')
    print(find_max(A, B))