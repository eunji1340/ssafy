def merge_sort(lft, rgt):
    if lft + 1 < rgt:
        mid = (lft + rgt) // 2
        merge_sort(lft, mid)
        merge_sort(mid, rgt)
        merge(lft, mid, rgt)

def merge(lft, mid, rgt):
    global arr, cnt
    
    L = arr[lft:mid]
    R = arr[mid:rgt]
    
    if L[-1] > R[-1]:
        cnt += 1
    
    i = j = 0
    k = lft
    
    while i < mid - lft and j < rgt - mid:
        if L[i] <= R[j]:
            arr[k] = L[i]
            k += 1
            i += 1
        else:
            arr[k] = R[j]
            k += 1
            j += 1
    
    while i < mid - lft:
        arr[k] = L[i]
        k += 1
        i += 1
        
    while j < rgt - mid:
        arr[k] = R[j]
        k += 1
        j += 1
        
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    merge_sort(0, N)
    print(f'#{tc} {arr[N//2]} {cnt}')