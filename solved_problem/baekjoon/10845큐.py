import sys
from collections import deque

sys.stdin=open('/Users/leesh970930/Desktop/coding_algorithm/solved_problem/baekjoon/input.txt', "r")
q=deque()
n=int(input())
for _ in range(n):
    command=list(map(str,input().split()))
    
    if command[0]=='push':
        q.append(int(command[1]))
    elif command[0]=='pop':
        if q: print(q.popleft())
        else: print(-1)
    elif command[0]=='size':
        print(len(q))
    elif command[0]=='empty':
        if q:print(0) 
        else: print(1)
        
    elif command[0]=='front':
        if q:print(q[0]) 
        else: print(-1)
    else:
         if q:print(q[-1])
         else: print(-1)