import sys

# 조카의 수, 과자의 수
m, n = map(int, sys.stdin.readline().split())
# 과자의 길이
arr = list(map(int, sys.stdin.readline().split()))
lt=1
rt=max(arr)
res=0

def Count(s):
    cnt=0
    for x in arr:
        cnt+=(x//s)
    return cnt

while lt<=rt:
    mid=(lt+rt)//2
    if mid==0:
        res=0
        break
    
    if Count(mid)>=m:
        lt=mid+1
        res=mid
    else:
        rt=mid-1
print(res)
