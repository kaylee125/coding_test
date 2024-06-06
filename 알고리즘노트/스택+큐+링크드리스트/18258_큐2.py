"""
문제설명: 정수를 저장하는 큐 구현
    push X: 정수 X를 큐에 넣는 연산이다.
    pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    size: 큐에 들어있는 정수의 개수를 출력한다.
    empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
    front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
핵심내용:
    deque로 구현
    
    push->append(x) 로 구현
    pop ->popleft()로 구현
    size -> len(deque())
    empty -> true/false로 구분
    front ->deque()[0] ->
    
"""

from collections import deque
import sys
# sys.stdin=open('input.txt','r')
N=int(input())
queue=deque() 

for _ in range(N):
    # x= input().split()
    cmd=list(map(str,sys.stdin.readline().split()))
    # x=sys.stdin.readline().split()
    

    if cmd[0]=='push':
        queue.append(cmd[1])

    elif cmd[0]=='front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif cmd[0]=='back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
    elif cmd[0]=='size':
        print(len(queue))
    elif cmd[0]=='empty':
        if queue:
            print(0)
        else:
            print(1)
    elif cmd[0]=='pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
            



