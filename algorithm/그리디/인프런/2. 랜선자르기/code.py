import sys 

base='/Users/leesh970930/Desktop/pythonalgorithm_formac/섹션 4/'
sys.stdin=open(base+'2. 랜선자르기/in1.txt', "r")

def Count(len):
    cnt=0
    for x in line:
        cnt+=(x//len) #각 랜선이 만들 수 있는 토막의 개수
    return cnt    

k,n=map(int,input().split())
line=[]
res=0
largest=0
for x in range(k):
    tmp=int(input())
    line.append(tmp)
    largest=max(largest,tmp)
lt=1
rt=largest

while lt<=rt:
    mid=(lt+rt)//2
    #자른 랜선의 갯수가 n보다 많은 경우(답이 되는 경우)
    if Count(mid)>=n:
        res=mid
        lt=mid+1

    #자른 랜선의 갯수가 n보다 적은 경우(답이 되지 않는 경우)
    else:
        rt=mid-1
print(res)
        
