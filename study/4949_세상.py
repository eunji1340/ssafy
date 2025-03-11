text = input()
while text != '.':
    stack = []
    result = 'yes'
    for c in text:
        if c in '([':
            stack.append(c)
        elif c in ')':
            if stack:
                if stack.pop() != '(':
                    result = 'no'
            else:
                result = 'no'
        elif c in ']':
            if stack:
                if stack.pop() != '[':
                    result = 'no'
            else:
                result = 'no'

    if stack:
        result = 'no'

    print(result)
    text = input()