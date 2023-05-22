import sys
sys.stdin=open('baekjoon/input.txt','r')

n,m=map(int,input().split())
arr=[i for i in range(1,n+1)]

for _ in range(m):
    i,j=map(int,input().split())
    tmp=arr[i-1]
    arr[i-1]=arr[j-1]
    arr[j-1]=tmp

for x in arr:
    print(x,end=' ')

