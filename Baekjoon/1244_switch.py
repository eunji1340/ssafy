# N = int(input())  # 스위치 개수
# switch = list(input().split())   # 스위치 상태
# stu_num = int(input())  # 학생 수
# student = [list(map(int, input().split())) for _ in range(stu_num)]
# switch.insert(0, 0)

# for i in range(stu_num):
#     num = student[i][1]
#     if student[i][0] == 1:
#         for j in range(1, N+1):
#             if j % num == 0:
#                 switch[j] = '1' if switch[j] == '0' else '0'
#
#     if student[i][0] == 2:
#         j = 0
#         while num - j >= 1 and num + j <= N:
#             if switch[num-j] != switch[num+j]:
#                 break
#             j += 1
#         j -= 1
#
#         for k in range(num-j, num+j+1):
#             switch[k] = '1' if switch[k] == '0' else '0'
#
# result = switch[1:]
# for i in range(0, len(result), 20):
#     print(*result[i:i+20])

N = int(input())
arr = [0] + list(map(int, input().split()))

M = int(input())

for _ in range(M):
    gender, num = list(map(int, input().split()))

    if gender == 1:
        for i in range(num, N+1, num):
            arr[i] = (arr[i] + 1) % 2
    elif gender == 2:
        arr[num] = (arr[num] + 1) % 2
        j = 1
        while num-j >= 1 and num+j <= N and arr[num-j] == arr[num+j]:
            arr[num-j] = (arr[num-j] + 1) % 2
            arr[num+j] = (arr[num+j] + 1) % 2
            j += 1

for i in range(1, N+1, 20):
    print(' '.join([str(n) for n in arr[i:i+20]]))