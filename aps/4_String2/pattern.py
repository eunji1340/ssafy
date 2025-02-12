# 패턴의 등장 횟수를 세는 고지식한 방법

t = 'TTTTTATTAATA'
p = 'TTA'
N = len(t)
M = len(p)
cnt = 0
for i in range(N-M+1):  # 비교 시작위치
    for j in range(M):
        if t[i + j] != p[j]:
            break    # for j, 다음 글자부터 비교 시작
    else:       # for j가 중단없이 반복되면
        cnt += 1        # 패턴 개수 1증가
print(cnt)

def patter_count(p,t):  # 패턴의 등장 횟수 리턴
    N = len(t)
    M = len(p)
    i = j = 0
    cnt = 0
    while i < N:
        if t[i] != p[j]:  # 다르면
            i = i - j + 1  # i - j 비교를 시작했던 위치
            j = 0
        else:  # 같으면
            i += 1
            j += 1
    if j == M:              # 패턴을 찾은 경우
        cnt += 1
        i = i - j + 1
        j = 0


def bruteforce(p, t):
    N = len(t)
    M = len(p)

    i = j =0
    while i < N and j < M:
        if t[i] != p[j]:   # 다르면
            i = i - j + 1  # i - j 비교를 시작했던 위치
            j = 0
        else:              # 같으면
            i += 1
            j += 1
    if j == M:
        return i-j      # 패턴의 시작 위치
    else:
        return -1

print(bruteforce(p, t))