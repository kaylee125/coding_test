N=int(input())
req=list(map(int,input().split()))
M=int(input())

lo=0
hi=max(req)
mid=(lo+hi)//2
ans=0
def is_possible(mid):
    """상한금액을 파라미터로 받았을때 
    각 지방마다 얼마를 줄지 
    그때의 국가총예산이 mid와 비교해서 미만인지 초과인지 판단 """
    total=0
    for r in req:
        total+=min(r,mid)
    
    return total<=M

while lo<=hi:
    print(f"lo:{lo} hi:{hi} mid:{mid} ans:{ans}")
    if is_possible(mid):
        lo=mid+1 #가능하다면 상한액 증가
        ans=mid
    else:
        hi=mid-1
    mid=(lo+hi)//2 #mid값 새로운 기준으로 갱신

print(ans)
    