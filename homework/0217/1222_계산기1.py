for tc in range(1, 11):
    N = int(input())
    fx = input()
    stack = []
    out = ''

    for x in fx:
        if x != '+':
            out += x
        else:
            if stack:
                out += stack.pop()
            stack.append(x)

    while stack:
        out += stack.pop()

    for x in out:
        if x != '+':
            stack.append(int(x))
        else:
            stack[-1] = stack[-1] + stack[-2]

    print(f'#{tc} {stack[-1]}')