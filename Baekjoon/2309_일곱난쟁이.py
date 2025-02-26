height = [int(input()) for _ in range(9)]

temp = []
for i in range(1<<9):
    temp = []
    for j in range(9):
        if i & (1<<j):
            temp.append(height[j])
    if len(temp) == 7 and sum(temp) == 100:
        temp.sort()
        break

for i in temp:
    print(i)