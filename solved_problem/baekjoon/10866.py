'''
덱: 양쪽에서 삽입,삭제 가능한 구조,스택과 큐의 기능을 모두 가지고 있고 
리스트에 비해 삽입,삭제 속도가 빠르다.
파이썬에서는 collections모듈에서 제공하는 deque로 선언하면 됨.
'''
import sys
from collections import deque

sys.stdin=open('/Users/leesh970930/Desktop/coding_algorithm/solved_problem/baekjoon/input.txt', "r")
input=sys.stdin.readline
q=deque()
n=int(input())
for _ in range(n):
    command=list(map(str,input().split()))
    
    if command[0]=='push_front':
        q.appendleft(int(command[1]))
    elif command[0]=='push_back':
        q.append(int(command[1]))
    elif command[0]=='pop_front':
        if q: print(q.popleft())
        else: print(-1)
    elif command[0]=='pop_back':
        if q: print(q.pop())
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