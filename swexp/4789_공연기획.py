T = int(input())

<<<<<<< HEAD
for tc in range(1, T + 1):
=======
for tc in range(1, T+1):
>>>>>>> b48cdedd4723ffb934175465d1ac69469550a5af
    arr = list(map(int, input()))
    ct = 0
    result = 0

    for i in range(len(arr)):
<<<<<<< HEAD
        if ct < i:
            result += (i - ct)
            ct += (i - ct)

        ct += arr[i]


    print(f'#{tc} {result}')
=======
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
>>>>>>> b48cdedd4723ffb934175465d1ac69469550a5af
