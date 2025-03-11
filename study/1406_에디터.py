string = list(input())
M = int(input())

left = string
right = []

for _ in range(M):
    command = input().split()

    t = command[0]
    if t == 'L':
        if left:
            right.append(left.pop())
    elif t == 'D':
        if right:
            left.append(right.pop())
    elif t == 'B':
        if left:
            left.pop()
    elif t == 'P':
        left.append(command[1])

print("".join(left+right[::-1]))