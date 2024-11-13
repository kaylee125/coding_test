
from collections import deque

dy=(0,1,0,-1)
dx=(1,0,-1,0)
chk=[[False]*100 for _ in range(100)]
N=int(input())

def is_valid(y,x):
    return 0<=y<N and 0<=x<N

def bfs(start_y,start_x):
    q=deque()
    q.append((start_y,start_x))

    while len(q)>0:
        y,x=q.popleft()
        chk[y][x]=True #방문표시
        for k in range(4): # 현재 좌표에서 for문으로 상하좌우 방문->좌표가 유효하고 아직 방문하기 전의 좌표일 경우 q에 좌표 추가
            ny=y+dy[k]
            nx=x+dx[x]
            if is_valid(ny,nx) and not chk[ny][nx]:
                q.append((ny,nx))
