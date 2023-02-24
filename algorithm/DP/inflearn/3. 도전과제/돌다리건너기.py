import sys
input=sys.stdin.readline

'''
돌다리를 다 건너려면 n까지가 아니라 n+1까지의 dynamic 값을 리턴해야함
'''
n=int(input())
dp=[0]*(n+2)
dp[1]=1
dp[2]=2

for i in range(3,n+2):
    dp[i]=dp[i-1]+dp[i-2]

print(dp[n+1])