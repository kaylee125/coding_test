'''
BFS:넓이 우선 탐색
- 레벨별로 오르쪽에서 왼쪽 순서로 탐색한다.
- deque 사용

'''
import sys
from collections import deque
sys.stdin=open('7. 송아지 찾기/in1.txt','r')


MAX = 10000
ch = [0] * (MAX+1) #해당 거리에 방문했는지 check
dis = [0] * (MAX+1)#몇번의 점프로 해당 거리에 도착했는지 점프의 갯수 표시
n,m = map(int,input().split()) #출발지점,도착지점
ch[n] = 1 #출발지점은 방문했으니깐 check
dis[n] = 0 #출발지점은 점프의 갯수가 0임
dQ = deque()
dQ.append(n)#큐에 출발점 추가

while dQ:
    now = dQ.popleft()#하나 꺼내서
    if now==m:
        break
    for next in (now-1, now+1, now+5):#3갈래로 방문
        if 0 <= next <= MAX:
            if ch[next]==0:#방문을 안한 지점일때만 큐 append
                dQ.append(next)
                ch[next] = 1#방문했으니깐 check
                dis[next] = dis[now]+1#점프의 갯수 갱신
                
print(dis[m])