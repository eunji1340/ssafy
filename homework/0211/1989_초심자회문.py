T = int(input())

for tc in range(1, T+1):
    string = input()
    n = len(string)
    result = 0

    for i in range(n//2):
        if string[i] != string[-1-i]:
            break
    else:
        result = 1

    print(f'#{tc} {result}')