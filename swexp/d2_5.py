T = int(input())

for test_case in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())
    print(f'#{test_case}', end=' ')
    A = W * P
    
    if W <= R:
        B = Q 
    else:
        B = Q + (W - R)*S
    
    if A < B:
        print(A)
    else:
        print(B)