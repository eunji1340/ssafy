import sys
input = sys.stdin.readline

K = int(input())

def recur(idx):
    if idx == 0:
        return 0
    if idx % 2:
        return 1 - recur(idx // 2)
    else:
        return recur(idx // 2)

print(recur(K - 1))

'''
X = 0 1 1 0 1 0 0 1 1 0 ...
1번 인덱스의 값은 1 → 0(= 1//2)번 인덱스의 값(=0)의 반대값
2번 인덱스의 값은 1 → 1(= 2//2)번 인덱스의 값(=1)과 같은 값
3번 인덱스의 값은 0 → 1(= 3//2)번 인덱스의 값(=1)의 반대값
즉, 홀수번째 오는 수는 //2 했을 때의 수와 반대이고
짝수번째 오는 수는 //2 했을 때의 수와 같다.
'''

'''
직접 문자열 다 구하기 -> 시간 초과
K = int(input())

def recur(x):
    if len(x) >= K:
        return x[K - 1]
    rev_x = ''.join('1' if num == '0' else '0' for num in x)
    return recur(x + rev_x)

print(recur('0'))
'''

#참고
#https://cheon2308.tistory.com/entry/%EB%B0%B1%EC%A4%80-18222%EB%B2%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%88%AC%EC%97%90-%EB%AA%A8%EC%8A%A4-%EB%AC%B8%EC%9E%90%EC%97%B4

