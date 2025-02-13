N = int(input())
P = list(map(int, input().split()))
time = [P[0]] * N

P.sort()

temp = 0
for i in range(N):
    time[i] = temp + P[i]
    temp = time[i]

print(sum(time))