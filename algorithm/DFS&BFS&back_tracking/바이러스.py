"""
[문제명] BOJ 2606 - 바이러스

문제 설명:
- n개의 컴퓨터, m개의 연결쌍이 있는 네트워크
- 1번 컴퓨터가 바이러스 걸리면 연결되어있는 모든 컴퓨터도 바이러스 걸림
- 1번 컴퓨터가 바이러스 걸렸을때 바이러스 걸리는 총 컴퓨터의 수 구함

입력: 
첫번째 줄 : 컴퓨터 수 
두번째 줄: 연결되어있는 컴퓨터 쌍의 수
세번째 줄~: 한 줄에 한 쌍씩 연결되어있는 컴퓨터의 쌍

출력:
바이러스 걸리는 총 컴퓨터의 수

해결 아이디어 (BFS):
- '1'인 지점을 시작점으로 BFS 실행
- 탐색 중 방문한 칸 수 = 그림의 넓이
- 모든 '1'에 대해 BFS 반복하며 최대 넓이 갱신

시간 복잡도:
- O(N*M): 모든 칸을 한 번씩 방문

예제:
입력:
7
6
1 2
2 3
1 5
5 2
5 6
4 7

출력:
4
"""
from collections import deque

n=int(input())
pairs=int(input())
graph=[[] for _ in range(n+1)]
visited=[0 for _ in range(n+1)]

pair_list=[tuple(map(int,input().split())) for _ in range(pairs) ]

for x,y in pair_list:
    graph[x].append(y)
    graph[y].append(x)

q = deque([1])
visited[1]=1
result=0

while q:
    node=q.popleft()

    for x in graph[node]:   
        if visited[x]==0:
            q.append(x)
            visited[x]=1
            result+=1


print(result)


