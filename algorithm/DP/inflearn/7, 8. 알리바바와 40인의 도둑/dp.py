import sys 

base='/Users/leesh970930/Desktop/pythonalgorithm_formac/섹션 8/'
sys.stdin=open(base+'7, 8. 알리바바와 40인의 도둑/in1.txt', "r")

'''
이중배열로 풀기
dp[0][i], dp[i][0]값을 먼저 a값으로 초기화 시킨 후
각 격자별로 에너지의 최소량인 경우의 에너지값을 저장한다.

'''
n=int(input())
a=[]
for _ in range(n):
   a.append(list(map(int,input().split())))

dp=[[0]*n for _ in range(n)]
dp[0][0]=a[0][0] #0행 0열 초기화

#dp[0][i], dp[i][0]값을 먼저 a값으로 초기화
for i in range(n):
    dp[0][i]=dp[0][i-1]+a[0][i]
    dp[i][0]=dp[i-1][0]+a[i][0]


for i in range(1,n):
    for j in range(1,n):
        dp[i][j]=min(dp[i-1][j],dp[i][j-1])+a[i][j]

print(dp[n-1][n-1])
