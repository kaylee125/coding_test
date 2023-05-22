import sys
from collections import deque
n,k=map(int,input().split())
arr=deque([i for i in range(1,n+1)])
cnt=0
ans=[]
while arr:
    for _ in range(k-1):
        arr.append(arr.popleft())
    ans.append(arr.popleft())
print("<", end='')
print(*ans, sep=', ', end = '')
print(">")

    


