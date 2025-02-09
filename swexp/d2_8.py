def find_pattern(string):
    result = ''
    for i in len(string):
        result = string[:i]
        if result == string[i:i+len(result)]:
            
        
T = int(input())

for test_case in range(1, T+1):
    print(f'#{test_case}', end = ' ')
    string = input()
    print(find_pattern(string))