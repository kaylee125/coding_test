import sys
sys.stdin=open('baekjoon/input.txt','r')
from collections import deque

T=int(input())
for _ in range(T):
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))
    q=deque()
    for i in range(n):
        q.append((i,arr[i]))
    cnt=0
    v=q[m]#q의 m번째 문서 정보 저장
    while q:
        max_q=max(q,key=lambda x:x[1]) 
        x=q.popleft() #(0, 5) 문서번호,중요도
        if x[1]==max_q[1]:
            cnt+=1
            if x==v:
                print(cnt)
                break
        else:
            q.append(x)

    
