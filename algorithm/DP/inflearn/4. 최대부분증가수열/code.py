
import sys 

base='/Users/leesh970930/Desktop/pythonalgorithm_formac/섹션 8/'
sys.stdin=open(base+'4. 최대부분증가수열/in1.txt', "r")

n=int(input())
a=list(map(int,input().split()))
a.insert(0,0)#1번째 원소를 인덱스1에 위치시키기 위해 
dp=[0]*(n+1)
dp[1]=1
res=0

for i in range(2,n+1):
    max=0
    for j in range(i-1,0,-1):
        #a[j]<a[i] 조건이 성립해야 a[j]가 a[i]의 앞항이 될 수 있음
        #a[j]<a[i]을 만족하는 여러개의 j값 중 수열의 길이가 가장 긴(max)를 찾아야함.
        if a[j]<a[i] and dp[j] >max:
            max=dp[j]
        dp[i]=max+1 #수열의 길이가 가장 긴 값을 찾았으면 그 값에 1을 더해주면 현재 i값의 최대수열의 길이라 됨
    if dp[i]>res:
        res=dp[i]

print(res)
