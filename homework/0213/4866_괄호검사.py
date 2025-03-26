T = int(input())

for tc in range(1, T+1):
    string = input()

    def find_bracket(string):
        stack = []
        result = 1
        for i in range(len(string)):
            if string[i] in '({':
                stack.append(string[i])
            elif string[i] in ')}':
                if stack[-1] == '(' and string[i] == ')':
                    stack.pop()
                elif stack[-1] == '{' and string[i] == '}':
                    stack.pop()
                else:
                    result = 0
                    return result

        if stack:
            result = 0

        return result

    print(f'#{tc} {find_bracket(string)}')