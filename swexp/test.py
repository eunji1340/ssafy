floor = [0,0,0,0]
floor[0:2] = 1
[floor[0:i] for i in range(2)] = 1
print(floor)