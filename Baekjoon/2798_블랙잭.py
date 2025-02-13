N, M = map(int, input().split())
number = list(map(int, input().split()))

result = 0
while True:
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                temp = number[i] + number[j] + number[k]
                if result < temp <= M:
                    result = temp
    else:
        break

print(result)


#print(number[i], number[j], number[k], temp)