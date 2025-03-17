T = int(input())


def quicksort(lft, rgt):
    if lft < rgt:  # 구간의 길이가 2 이상이라면
        # 주어진 배열을 [lft, rgt] 구간에 대해서 쪼갠다.
        # 가장 왼쪽 원소(lft 위치)를 pivot으로 삼고
        # pivot을 정렬된 위치에 놓고, pivot_idx를 반환
        pivot_idx = partition(lft, rgt)

        quicksort(lft, pivot_idx - 1)
        quicksort(pivot_idx + 1, rgt)


def partition(lft, rgt):
    global arr

    pivot = arr[lft]  # 해당 구간에서 가장 왼쪽에 있는 것을 기준점으로 한다.
    i = lft
    j = rgt

    while i < j:
        while i <= rgt and arr[i] <= pivot:
            i += 1

        while arr[j] > pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    # 정렬된 위치에 놓기
    arr[lft], arr[j] = arr[j], arr[lft]

    return j


for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 닫힌 구간 []을 사용용
    quicksort(0, N - 1)
    print(arr)