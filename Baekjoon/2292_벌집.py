# N = int(input())
# house = [[1]]
#
# i = 2
# ct = 1
# while i < N+1:
#     temp = []
#     for j in range(i, i+ct*6):
#         temp.append(j)
#     house.append(temp)
#     i = i + ct*6
#     ct += 1
#
# result = 0
# for i in range(len(house)):
#     if N in house[i]:
#         result = i + 1
#         break
#
# print(house)
# print(result)

N = int(input())

i = 1
ct = 1
while i < N:
    i += 6*ct
    ct += 1

print(ct)
