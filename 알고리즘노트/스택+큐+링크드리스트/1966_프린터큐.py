"""

헷갈리는 점: 순서를 보장하면서 몇번째로 출력되는지를 어떻게 구현해야하지?
 - enumerate활용법
 - while문을 사용한 이유:q의 길이가 매번 변경되기 때문에 이 경우는 while문을 사용하는게 적합함

    """
import sys
from collections import deque

sys.stdin=open('input.txt','r')

T=int(sys.stdin.readline().rstrip())

for _ in range(T):

    n,m=list(map(int,sys.stdin.readline().split())) #n:문서의 갯수 m:찾고자하는 인덱스/O(1)
    
    q=list(enumerate(list(map(int,sys.stdin.readline().split()))))
    q=deque(q) #O(n) n: 문서의 갯수
    cnt=1
    while q: # deque 내 각 문서에 대해 n번 반복 가능 /O(n)
        #나보다 큰 우선수위가 있다면 출력하지 않고 q의 마지막으로 이동
        max_prior=max(i[1] for i in q) #O(n)
        if q[0][1]<max_prior:
            q.append(q.popleft()) #O(1)
        #나의 우선수위가 가장 크다면 프린트 출력
        else:
            if q.popleft()[0]==m: #찾고자했던 m번째 인덱스의 문서가 몇번째로 출력되었는지 print
                print(cnt)
            cnt+=1