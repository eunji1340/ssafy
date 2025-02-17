stack = [0] * 100
top = -1
susik = '6528-*2/+'
for x in susik:
    if x not in '+-/*':  # 피연산자면
        top += 1         # push(x)
        stack[top] = int(x)
    else:                # 연산자인 경우
        op2 = stack[top] # pop(), 오른쪽 피연산자
        top -= 1
        op1 = stack[top] # pop(), 왼쪽 피연산자
        top -= 1
        if x == '+':  # op1 + op2
            top += 1                # push()
            stack[top] = op1 + op2
        elif x == '-':
            top += 1
            stack[top] = op1 - op2
        elif x == '/':
            top += 1
            stack[top] = op1 / op2
        elif x == '*':
            top += 1
            stack[top] = op1 * op2