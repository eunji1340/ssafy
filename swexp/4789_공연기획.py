T = int(input())

<<<<<<< HEAD
for tc in range(1, T+1):
=======
for tc in range(1, T + 1):
>>>>>>> 98c9168dc4165279994122d43c96725acd95b85c
    arr = list(map(int, input()))
    ct = 0
    result = 0

    for i in range(len(arr)):
<<<<<<< HEAD
        if arr[i] == 0 :
            continue
        else:
            if ct >= i:
                ct += arr[i]
            else:
                result += 1
                ct += 1

    print(f'#{tc} {result}')


T = int(input())  # 테스트 케이스 수

for tc in range(1, T + 1):
    arr = input().strip()  # 0과 9로 이루어진 문자열
    print(arr)
    ct = 0  # 박수를 해야하는 최소 사람 수
    for i in range(len(arr)):
        if arr[i] == '0' and ct <= i:
            ct += 1  # 박수하는 사람을 세어봄

    print(f'#{tc} {ct}')
=======
        if ct < i:
            result += (i - ct)
            ct += (i - ct)

        ct += arr[i]


    print(f'#{tc} {result}')
>>>>>>> 98c9168dc4165279994122d43c96725acd95b85c
