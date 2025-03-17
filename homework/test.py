arr = [5, 8, 1, 7, 3, 4, 2, 9]

pivot = arr[0]  # 0번 인덱스를 기준점으로 삼는다.

i = 0  # 왼쪽 포인터
j = len(arr) - 1  # 오른쪽 포인터

while i < j:  # 크로스가 발생하지 않을 때까지
    while arr[i] <= pivot:  # i는 pivot보다 큰 수를 찾아야 함. <=> pivot보다 작은수는 건너뛴다.
        i += 1

    while arr[j] > pivot:  # pivot보다 작은 수를 찾아야 하므로, pivot보다 큰수를 발견하면 건너뜀.
        j -= 1

    if i < j:  # 크로스가 발생하지 않았다면
        arr[i], arr[j] = arr[j], arr[i]

    print(f'swap ({i}, {j})')
    print(arr)

# pivot을 정렬된 위치에 놓아야 한다.
# 0번째, j번째를 바꾸면 됨
print(f'swap (0, {j})')
arr[0], arr[j] = arr[j], arr[0]
print(arr)