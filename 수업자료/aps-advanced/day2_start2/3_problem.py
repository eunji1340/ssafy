def solution():
    target = M
    for i in range(N):
        if target & 0x1 == 0:
            return False
        target = target >> 1
    return True

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = solution()
    print(result)

'''
5
4 0
4 30
4 47
5 31
5 62
'''