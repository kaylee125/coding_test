"""
### BFS(너비우선탐색방식)

- 구현방식
    - 큐를 이용해 구현
    - 루트 노드부터 시작하여 각 레벨의 노드를 순차적으로 방문
- 특징
    - 루트에서 가까운 노드부터 차례대로 탐색
- 응용
    - 최단 경로 문제 해결에 유용
    - 트리의 각 레벨에 있는 노드들을 순서대로 처리할 때 사용
"""
from collections import deque

adj=[[0]*13 for _ in range(13)] #인접행렬 생성
adj[0][1]=adj[0][2]=1
adj[1][3]=adj[1][4]=1

def bfs():
    dq=deque()
    dq.append(0) #루트 노드 삽입
    while dq:
        now=dq.popleft()
        for nxt in range(13):
            if adj[now][nxt]:
                dq.append(nxt)


bfs()