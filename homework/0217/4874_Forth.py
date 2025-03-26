T = int(input())
for tc in range(1, T + 1):
    cal = list(input().split())
    stack = []

    print(f'#{tc}', end=' ')
    for c in cal:
        if c == '.':  # '.'을 만나면 결과 출력
            if len(stack) == 1:  # 스택에 하나의 값만 남아있으면 결과 출력
                print(stack[0])
            else:
                print("error")
            break

        elif c not in '+-/*.':  # 숫자일 경우
            stack.append(int(c))

        else:  # 연산자일 경우
            if len(stack) < 2:  # 연산자가 나오기 전에 숫자가 두 개 이상 있어야 함
                print("error")
                break

            op2 = stack.pop()  # 두 번째 숫자
            op1 = stack.pop()  # 첫 번째 숫자

            if c == '+':
                stack.append(op1 + op2)
            elif c == '-':
                stack.append(op1 - op2)
            elif c == '/':
                if op2 == 0:  # 나누기 연산에서 0으로 나누는 경우
                    print("error")
                    break
                stack.append(op1 / op2)
            elif c == '*':
                stack.append(op1 * op2)