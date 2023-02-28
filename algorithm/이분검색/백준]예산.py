#배정된 예산 중 최댓값


import sys
input = sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))
budget=int(input())
lt=3
rt=max(arr)
res=0

def Count(bud): #mid값이 최대 예산금액일 경우 전체 예산 집행액(Total)
    total=0
    for x in arr:
        if x>bud:
            total+=bud
        else:
            total+=x
    return total

while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)<=budget:
        lt=mid+1
        res=mid
    else:
        rt=mid-1
print(res)
