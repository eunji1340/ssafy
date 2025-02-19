# 부분집합 재귀로 구현하기
def f(idx):
    if idx == N:
        print(out)
        return
    else:
        out[idx] = 1
        f(idx+1)
        out[idx] = 0
        f(idx+1)

arr = [1, 2, 3, 4, 5]
N = len(arr)
out = [False] * N

f(1)