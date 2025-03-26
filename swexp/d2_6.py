T = int(input())

def check(string):
    for i in range(len(string)//2):
        if string[i] != string[-(i+1)]:
            return 0
    return 1

for test_case in range(1, T+1):
    print(f'#{test_case}', end=' ')
    string = input()
    print(check(string))