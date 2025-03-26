L = int(input())
N = int(input())

cake = [0] * (L + 1)
count = ex_num = re_num = 0

for num in range(1,N+1):
    P, K = map(int, input().split())

    for i in range(L+1):
        if P <= i <= K and cake[i] == 0:
            cake[i] = num

    if count < (K - P + 1):
        count = (K - P + 1)
        ex_num = num

count = 0
for num in range(1, N+1):
    if count < cake.count(num):
        count = cake.count(num)
        re_num = num

print(ex_num)
print(re_num)