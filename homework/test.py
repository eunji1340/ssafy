N = int(input())
arr = list(map(int, input().split()))

# # bubble
# for i in range(N-1):
#     for j in range(i, N-1):
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]
#
# print(arr)

# # selection
# for i in range(N-1):
#     min_idx = i
#     for j in range(i+1, N):
#         if arr[min_idx] > arr[j]:
#             min_idx = j
#     arr[i], arr[min_idx] = arr[min_idx], arr[i]
#
# print(arr)

ct = [0] * (max(arr) + 1)
for i in range(N):
    ct[arr[i]] += 1

# 누적합
for i in range(1, max(arr)+1):
    ct[i] += ct[i-1]

result = [0] * N
for i in range(N-1, -1, -1):
    ct[arr[i]] -= 1
    result[ct[arr[i]]] = arr[i]
print(result)