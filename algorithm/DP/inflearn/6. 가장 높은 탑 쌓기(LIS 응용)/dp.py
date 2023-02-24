import sys 

base='/Users/leesh970930/Desktop/pythonalgorithm_formac/섹션 8/'
sys.stdin=open(base+'6. 가장 높은 탑 쌓기(LIS 응용)/in1.txt', "r")

n=int(input())
a=[]
for _ in range(n):
    x,h,w=map(int,input().split())
    a.append((x,h,w))
a.sort(reverse=True)
dp=[0]*(n)
dp[1]=a[0][1] #1번째 높이 초기화
res=0

for i in range(1,n):
    max_h=0
    for j in range(i-1,-1,-1):
        if a[i][2]< a[j][2] and max_h <dp[j]:
            max_h=dp[j]
    dp[i]=max_h+a[i][1]
    
    if res<dp[i]:
        res=dp[i]
print(res)