def find_k(num):  # 이진수 K의 최대길이를 반환하는 함수
    max_ct = 0  # 최대길이를 저장할 변수
    start = 0  # 이진수 K의 시작 위치
    while start < N:  # 시작 위치가 N보다 작을 때 까지만
        if num[start] == '1':  # 1을 찾았을 때 -> 시작
            for i in range(start + 1, N):  # 시작위치 다음부터
                if num[i] == '1':  # 1을 찾으면 마지막 위치로 저장
                    end = i
                    if num[start:end + 1].count('1') != K:  # 만약 1의 개수가 K개가 아니면 패스
                        continue
                    max_ct = max(max_ct, end - start + 1)  # 최대 길이을 저장
        start += 1  # 시작 위치 이동

    return max_ct

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())  # 이진수 길이, 필요한 1의 개수
    bin_num = input()  # 이진수
    print(f'#{tc} {find_k(bin_num)}')