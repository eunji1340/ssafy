for tc in range(1, 11):
    N = int(input())
    fx = input()
    stack = [0] * 100
    susik = ''
    top = -1

    for x in fx:
        if x not in '+*':
            susik += x
        elif x == '*':
            while top > -1 and stack[top] == '*':
                susik += stack[top]
                top -= 1
            top += 1
            stack[top] = x
        elif x == '+':
            while top > -1:
                susik += stack[top]
                top -= 1
            top += 1
            stack[top] = x

    while top > -1:
        susik += stack[top]
        top -= 1

    for x in susik:
        if x not in '+*':
            top += 1
            stack[top] = int(x)
        else:
            op2 = stack[top]
            top -= 1
            op1 = stack[top]

            if x == '*':
                stack[top] = op1 * op2
            else:
                stack[top] = op1 + op2

    print(f'#{tc} {stack[top]}')



