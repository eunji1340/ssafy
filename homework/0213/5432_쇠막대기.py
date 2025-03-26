T = int(input())
for tc in range(1, T+1):
    stick = list(input())
    stack = []
    ct = 0

    for i in range(len(stick)):
        if stick[i] == '(':
            stack.append('(')
        else:
            stack.pop()
            if stick[i-1] == '(':
                ct += len(stack)
            else:
                ct += 1

    print(f'#{tc} {ct}')