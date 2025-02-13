arr = [int(input()) for _ in range(10)]

score = arr[0]
for i in range(9):
    if abs(100 - (score + arr[i+1])) <= abs(100 - score):
        score += arr[i+1]
    else:
        break

print(score)