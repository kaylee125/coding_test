import sys 

base='/Users/leesh970930/Desktop/pythonalgorithm_formac/섹션 4/'
sys.stdin=open(base+'3. 뮤직비디오/in1.txt', "r")

def Count(capacity):
    cnt=1
    sum=0
    for x in a:
        if sum+x>capacity: 
            cnt+=1 #새로운 DVD 하나 추가
            sum=x #추가된 DVD의 첫곡은 x임
        else:
            sum+=x
    return cnt

n,m=map(int,input().split())
a=list(map(int,input().split()))
lt=1
rt=sum(a)
res=0
maxx=max(a)

while lt<=rt:
    mid=(lt+rt)//2 #mid=DVD용량
    if Count(mid)<=m and mid>=maxx:
        res=mid
        rt=mid-1 #큰 쪽을 버려야함
    else: #용량이 작아서 더 큰 쪽을 살펴야함
        lt=mid+1

print(mid)

