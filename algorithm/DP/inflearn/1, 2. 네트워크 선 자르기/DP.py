import sys
input = sys.stdin.readline

'''
다이나믹 프로그래밍으로 풀이
점화식 : f(n)=f(n-1)+f(n-2)
'''
n=int(input())
line=[0]*(n+1)
line[1]=1
line[2]=2

for i in range(3,n+1):
    line[i]=line[i-1]+line[i-2]

print(line[n])