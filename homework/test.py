def find(left,right,target,prev):
    if left>right:
        return False
    mid=(left+right)//2
    if lst_n[mid]==target:
        return mid
    if target >lst_n[mid]:#오른쪽 탐색색
        if prev==1:
            return False
        return find(mid+1,right,target,1)
    else:#왼쪽 탐색색
        if prev==0: 
            return False
        return find(left,mid-1,target,0)
def find2(target):
    left=0
    right=n-1
    prev=None
    while left<=right:
        mid=(left+right)//2
        if lst_n[mid]==target:
            return mid
        if target >lst_n[mid]:
            if prev==1:
                return False
            prev=1
            left=mid+1
        else:
            if prev==0:
                return False
            prev=0
            right= mid-1
    return False
t=int(input())
for test in range(1,t+1):
    n,m=map(int,input().split())
    lst_n=list(map(int,input().split()))
    lst_m=list(map(int,input().split()))
    lst_n.sort()
    cnt=0
    cnt2=0
    for i in range(m):
        if find(0,n-1,lst_m[i],100) is not False:
            cnt+=1
    # for i in range(m):
    #     res=find2(lst_m[i])
    #     if res is False:
    #         continue
    #     else:
    #         cnt2+=1
    print(f"#{test} {cnt}")
    # print(f"#{test} {cnt2}")