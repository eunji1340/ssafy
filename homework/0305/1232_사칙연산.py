def pre_order(i):
    global ct
    lft = 2*i
    rgt = 2*i + 1
    
    if lft <= N:
        pre_order(lft)
        

for tc in range(1, 11):
    N = int(input())  # 정점의 개수
    
'''
def inorder(i):
    lft = 2*i # 왼쪽 자식 (배열의 인덱스 범위 안에 있다면)
    rgt = 2*i + 1 #오른쪽 자식

    # 왼쪽 트리 먼저 순회
    if lft <= N: # 왼쪽 자식이 있다면
        inorder(lft) # 왼쪽 자식을 기준으로 중위순회
    
    # 자기자신 순회 
    tree[i] = cnt
    cnt += 1

    # 오른쪽 트리 순회
    if rgt <= N: # 오른쪽 자식이 있다면
        inorder(rgt)

'''