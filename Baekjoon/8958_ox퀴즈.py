T = int(input())
for tc in range(T):
    string = input()
    ct = 0
    result = []
    for i in range(len(string)):
        if string[i] == 'O':
            ct += 1
            result.append(ct)
        else:
            ct = 0
            result.append(ct)
    print(sum(result))