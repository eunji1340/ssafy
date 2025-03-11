import sys
#sys.stdin = open('input.txt', 'r')

N = int(input())
arr = list(map(int, input().split()))

def share_snack():
    stack = []
    num = 1

    for i in range(N):
        while stack and stack[-1] == num:
            stack.pop()
            num += 1
        if arr[i] == num:
            num += 1
        else:
            stack.append(arr[i])

    while stack:
        if stack.pop() != num:
            return 'Sad'
        num += 1

    return 'Nice'

print(share_snack())