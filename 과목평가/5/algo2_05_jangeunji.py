def pre_order(i, tree):  # 전위순회
    if i > N:  # 인덱스가 N 이상이면 리턴
        return
    tree.append(arr[i-1])
    pre_order(i * 2, tree)
    pre_order(i * 2 + 1, tree)
    return tree  # 이진수 배열을 리턴

def in_order(i, tree):  # 중위순회
    if i > N:
        return
    in_order(i * 2, tree)
    tree.append(arr[i - 1])
    in_order(i * 2 + 1, tree)
    return tree

def post_order(i, tree):  # 후위순회
    if i > N:
        return
    post_order(i * 2, tree)
    post_order(i * 2 + 1, tree)
    tree.append(arr[i - 1])
    return tree

def bin_to_dec(arr):
    num = ''.join(arr)  # 배열을 문자열로 바꾸기
    ans = pow = 0
    for i in range(len(num)-1, -1, -1):  # 뒤에서부터 읽기
        if num[i] == '1':  # 만약 1이면 결과값에 더하기
            ans += 2 ** pow
        pow += 1  # 지수 더하기
    return ans

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 정점 개수
    arr = input().split()  #각 정점의 값
    bin_arr = [pre_order(1, []), in_order(1, []), post_order(1, [])]  # 각 순회 결과 리스트
    max_num = 0  # 최대 숫자 저장할 변수
    for num in bin_arr:  # 각 순회 결과를 10진수로 바꾸고 최대 숫자 구하기
        max_num = max(max_num, bin_to_dec(num))

    print(f'#{tc} {max_num}')