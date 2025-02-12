T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    length = len(str1)
    result = 0

    for i in range(len(str2)-length):
        if str2[i:i+length] == str1:
            result = 1

    print(f'#{tc} {result}')

