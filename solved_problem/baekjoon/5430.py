import sys
sys.stdin=open('baekjoon/input.txt','r')
from collections import deque
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    cmds=input()
    n=int(input())
    arr = deque(input().rstrip()[1:-1].split(","))
    if n==0: 
        arr=deque()
    res=True
    r_cnt=0
    for cmd in cmds:
        if cmd=='R':
            r_cnt+=1
            if r_cnt%2==1:
                arr.reverse()
        if cmd=='D':
            if arr:
                arr.popleft()
            else:
                res=False
                print('error')
                break
    if res:
        print('['+','.join(arr)+']')