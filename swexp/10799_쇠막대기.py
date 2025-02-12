T = int(input())

for tc in range(1, T+1):
    laser = input()
    stack = []
    ct = 0
    for i in range(len(laser)):
        if laser[i] == '(':
            stack.append('(')
        else:
            stack.pop()
            if laser[i-1] == '(':
                ct += len(stack)
            else:
                ct += 1

    print(f'#{tc} {ct}')