"""
📝 1. BFS 문제를 푸는 공식적인 절차

① 문제 이해:
그래프 형태 확인: 2D 격자, 트리, 그래프(노드와 간선) 중 무엇인지 파악
이동 조건 및 탐색 범위: 상하좌우, 대각선 이동, 또는 특정 조건 충족 시 이동 등

② 자료구조 및 패턴 기억:
Queue (collections.deque) 사용: BFS는 FIFO(First-In, First-Out) 구조
방문 여부 (visited 배열) 반드시 사용: 중복 방문 방지
거리 기록: 이전 노드의 거리에서 +1을 더해 저장 (최단거리 문제일 때)

③ 상하좌우(또는 대각선) 방향 벡터 정의:
directions = [(1,0), (-1,0), (0,1), (0,-1)]

④ 출발지(시작점)를 Queue에 삽입 후 BFS 탐색:
while queue: 형태의 반복문 사용
popleft()로 현재 노드 꺼내기
for dx, dy in directions:으로 주변 탐색

⑤ 조건에 따른 종료 및 결과 반환:
모든 노드를 탐색 후 조건에 맞는 값을 반환
최단 거리라면 graph[n-1][m-1] 반환

**실전전략**
✅ 반드시 Queue (deque) 사용: popleft()로 시간 효율 향상
✅ visited 배열을 사용해 중복 탐색 방지
✅ 2D 배열 문제는 for문 중첩보다 방향 벡터 사용
✅ graph[x][y] = graph[prev_x][prev_y] + 1로 거리 계산
✅ 여러 시작점은 초기에 모두 큐에 삽입 (다중 출발지 문제)
✅ 출력 시 조건에 맞지 않으면 즉시 return으로 중단
"""

from collections import deque

def bfs(start_x,start_y,graph):
    n,m=len(graph),len(graph[0]) #행,렬 갯수

    visited=[[False]*m for _ in range(n)]
    directions=[(1,0),(-1,0),(0,1),(0,-1)] #상하좌우

    queue=deque([(start_x,start_y)])
    while queue:
        x,y=queue.popleft()

        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if graph[nx][ny]==1: #조건에 맞는 경우 
                    visited[nx][ny]=True #방문처리
                    queue.append((nx,ny)) #다시 반복될수있도록 queue에 신규좌표 삽입

                