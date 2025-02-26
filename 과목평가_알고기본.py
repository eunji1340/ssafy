# 버블 정렬
arr1 = [55, 7, 78, 12, 42]
N1 = len(arr1)

def bubble_sort(a, N):
    for i in range(N-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

#print(bubble_sort(arr1, N1))

# 카운팅 정렬
arr2 = [0,4,1,3,1,2,4,1]
N2 = len(arr2)

def counting_sort(a, N):
    count = [0] * (max(a)+1)
    sort_arr = [0] * N

    for i in range(N):
        count[a[i]] += 1

    for i in range(1, len(count)):
        count[i] += count[i-1]

    for i in range(N-1, -1, -1):
        count[a[i]] -= 1
        sort_arr[count[a[i]]] = a[i]

    return sort_arr

#print(counting_sort(arr2, N2))

# 선택 정렬
def selection_sort(a, N):
    for i in range(N-1):
        min_idx = i
        for j in range(i+1, N):
            if a[min_idx] > a[j]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

#print(selection_sort(arr1, N1))

# 순차 검색
# 정렬 x
def sequential_search(a, N, key):
    for i in range(N):
        if a[i] == key:
            return i
    return

# 정렬 o
def sequential_search2(a, N, key):
    a.sort()
    for i in range(N):
        if a[i] == key:
            return i
        elif a[i] > key:
            return
    return

#print(sequential_search(arr1, N1, 78))
#print(sequential_search2(arr1, N1, 78))

# 이진 검색
def binary_search(a, N, key):
    a.sort()
    start = 0
    end = N-1
    while start <= end:
        middle = (start + end) // 2
        if a[middle] == key:
            return middle
        elif a[middle] < key:
            start = middle + 1
        else:
            end = middle - 1
    return

#print(binary_search(arr1, N1, 42))

# 고지식한 알고리즘
t = 'TTTTTATTAATA'   # 전체 문자열
p = 'TTA'            # 찾을 패턴

def bruteforce(t, p):
    N = len(t)
    M = len(p)

    i = j = 0
    while i < N and j < M:
        if t[i] != p[j]:
            i = i - j + 1
            j = 0
        else:
            i += 1
            j += 1
    if j == M:
        return i-j
    else:
        return -1

#print(bruteforce(t, p))

def bruteforce2(t, p):
    N = len(t)
    M = len(p)

    for i in range(N-M+1):
        for j in range(M):
            if t[i+j] != p[j]:
                break
        else:
            return i
    return

#print(bruteforce2(t, p))

def pattern_count(t, p):
    N = len(t)
    M = len(p)

    ct = 0
    i = j = 0
    while i < N and j < M:
        if t[i] != p[j]:
            i = i - j + 1
            j = 0
        else:
            i += 1
            j += 1
        if j == M:
            ct += 1
            i = i - j + 1
            j = 0

    return ct

#print(pattern_count(t, p))

def pattern_count2(t, p):
    N = len(t)
    M = len(p)
    ct = 0
    for i in range(N-M+1):
        for j in range(M):
            if t[i+j] != p[j]:
                break
        else:
            ct += 1

    return ct

#print(pattern_count2(t, p))

# KMP 알고리즘
def kmp(t, p):
    N = len(t)
    M = len(p)
    lps = [0] * (M+1)

    j = 0
    lps[0] = -1
    for i in range(1, M):
        lps[i] = j
        if p[i] == p[j]:
            j += 1
        else:
            j = 0
    lps[M] = j
    print(lps)
    i = j = 0
    while i < N and j < M:
        if j == -1 or t[i] == p[j]:
            i += 1
            j += 1
        else:
            j = lps[j]
        if j == M:
            print(i-M, end = ' ')
            j = lps[j]
    print()
    return

kmp('zzzabcdabcdabcefabcd', 'abcdabcef')