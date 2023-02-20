'''
1.아이디어:
- 토막낼 랜선의 최대 길이는 arr중 가장 짧은 랜선이다.max(arr)
- 0~max(arr)중 n개 이상의 토막을 낼 수 있는 최대길이를 구한다
- 랜선의 갯수를 구하는 함수 Count()를 따로 정의한다

'''
import sys 

base='/Users/leesh970930/Desktop/pythonalgorithm_formac/섹션 4/'
sys.stdin=open(base+'2. 랜선자르기/in1.txt', "r")

def Count(len):
    cnt=0 #len으로 전체 랜선 k개를 토막냈을 경우 랜선의 갯수
    for i in arr:
        cnt+=(i//len)
        
    return cnt
    
k,n=map(int,input().split())
arr=[]
for _ in range(k):
    arr.append(int(input()))

largest=max(arr) #랜선이 아무리 길어도 가장 긴 랜선을 넘어가진 않음
lt=0
rt=largest
res=0 #토막낸 랜선의 길이

while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=n:
        res=mid 
        lt=mid+1
    else:
        rt=mid-1
print(res)

