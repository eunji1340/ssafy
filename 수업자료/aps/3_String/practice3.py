t = 'EOGGXYPVSY'
p = 'XYPV'

def serch(p, t):
    N = len(t)
    M = len(p)
    for i in range(N-M+1):  # t에서 패턴을 비교할 시작 위치 인덱스
        for j in range(M):  # p에서 비교할 위치 인덱스
            if t[i+j] != p[j]:
                break
        else:               # break에 걸리지 않고 for가 끝난 경우 실행
            return i        # 패턴이 처음 나타난 인덱스 리턴
    return -1

print(serch(p, t))