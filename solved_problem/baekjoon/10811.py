import sys
sys.stdin=open('baekjoon/input.txt','r')

n,m= map(int,input().split())
arr=[i for i in range(1,n+1)]

for _ in range(m):
    i,j=map(int,input().split())
    
    r=j-i+1
    for _ in range(r//2): ## r//2번만 반복만을 돌리면서 값을 변경하면 됨.
        tmp=arr[i-1]
        arr[i-1]=arr[j-1]
        arr[j-1]=tmp
        i+=1
        j-=1
for x in arr:
    print(x,end=' ')