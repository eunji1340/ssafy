def find_position(d, l):
    if d == 1:
        return l
    elif d == 4:
        return width + l
    elif d == 2:
        return width * 2 + height - l
    elif d == 3:
        return width * 2 + height * 2 - l

width, height = map(int, input().split())
n = int(input())
store = [list(map(int, input().split())) for _ in range(n)]
pd, pl = map(int, input().split())
p_pos = find_position(pd, pl)

total = 0
length = width * 2 + height * 2
for d, l in store:
    s_pos = find_position(d, l)
    distance = min(abs(p_pos - s_pos), length - abs(p_pos - s_pos))
    total += distance

print(total)
