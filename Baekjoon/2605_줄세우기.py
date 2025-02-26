N = int(input())
number = list(map(int, input().split()))
result = [1]

for i in range(N):
    if number[i] == 0:
        result.append(i+1)
    else:
        result.insert(-number[i], i+1)

print(*result[1:])