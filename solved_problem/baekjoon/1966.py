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
    # m번 문서가 몇번째로 출력되는지 확인
    # popleft()한 문서가 우선순위가 가장 크면 count 아니면 arr.append(arr.popleft())
    cnt=0
     #가장 큰 중요도
    while q:
        max_q=max(q,key=lambda x:x[1])
        x=q.popleft() #(0, 5) 문서번호,중요도
        if not q:#arr의 원소가 1개인 경우
            cnt=1
            break
        if x[1]>=max_q[1]:
            cnt+=1#우선순위가 가장 커서 출력대기열에서 삭제될 경우 
            if x[0]==m:
                break
        else:
            q.append(x) #큐의 뒤로 다시 재배치 
        

    print(cnt)
