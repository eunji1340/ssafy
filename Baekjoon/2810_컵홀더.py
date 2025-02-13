N = int(input())  # 좌석 수
sit = [0] + list(input()) + [0]

ct = 0
i = 0
while i <= N:
    if sit[i] == 0 or sit[i] == 'S':
        ct += 1
    else:
        i += 1
        ct += 1
    i += 1

if ct > N:
    ct = N

print(ct)