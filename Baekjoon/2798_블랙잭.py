N, M = map(int, input().split())
number = list(map(int, input().split()))

result = 0
while True:
    temp = 0
    for i in range(N-2):
        temp += number[i]
        for j in range(i, N-1):
            temp += number[j]
            for k in range(i, N):
                temp += number[k]

                if result < temp < M:
                    result = temp

print(result)