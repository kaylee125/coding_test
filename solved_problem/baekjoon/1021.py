import sys
sys.stdin=open('baekjoon/input.txt','r')
from collections import deque
n,m=map(int,input().split())
numbers=list(map(int,sys.stdin.readline().split()))
q=deque([i for i in range(1,n+1)])
#n개의 수를 돌면서 q를 차례대로 출력시킴
#q의 값이 n개의 수에서 몇번째 인덱스에 있는지 확인
#len(q)//2값보다 큰지 작은지 판별
cnt=0
while numbers:
    num=numbers.pop(0)
    while True:
        if num==q[0]:
            q.popleft()
            break
        if q.index(num)>len(q)//2:
            q.appendleft(q.pop())
            cnt+=1
        else:
            q.append(q.popleft())
            cnt+=1
print(cnt)
        

