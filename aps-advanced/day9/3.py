import heapq

arr = [20, 15, 19, 4, 13, 11]

heapq.heapify(arr)
print(arr)

min_heap = []
max_heap = []
for num in arr:
    heapq.heappush(min_heap, num)
    heapq.heappush(max_heap, num)
print(min_heap)
print(max_heap)

