arr = []
for i in range(10):
    arr.append(int(input()))

rest = []
for n in arr:
    rest.append(n % 42)

print(len(set(rest)))