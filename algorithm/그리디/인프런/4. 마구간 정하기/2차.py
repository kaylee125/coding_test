import sys 

base='/Users/leesh970930/Desktop/pythonalgorithm_formac/섹션 4/'
sys.stdin=open(base+'4. 마구간 정하기/in2.txt', "r")

def Count(d):
    #말의 개수
    cnt=1
    endpoint=a[0]
    for x in range(1,n):
        #리스트의 인접한 두 원소값의 차이(말이 배치된 거리)가 매개변수 d 이상이면 말을 배치한다.
        if a[x]-endpoint>=d:
            cnt+=1
            endpoint=a[x] #endpoint 갱신
    return cnt


n,c=map(int,input().split())
a=[]
for _ in range(n):
    a.append(int(input()))
a.sort()
lt=1
rt=max(a)
res=0

while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=c: #mid 거리간격으로 말을 배치했을때 c마리 이상 배치 가능한지 
        res=mid
        lt=mid+1
    else:
        rt=mid-1
print(res)


