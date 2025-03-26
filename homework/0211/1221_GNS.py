T = int(input())

for tc in range(1, T+1):
    n = int(list(input().split())[-1])
    arr = list(input().split())
    number = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    count = [0] * 10

    for i in range(10):
        count[i] = arr.count(number[i])

    result = ''

    for i in range(10):
        for _ in range(count[i]):
            result += number[i] + ' '

    print(f'#{tc}')
    print(result)