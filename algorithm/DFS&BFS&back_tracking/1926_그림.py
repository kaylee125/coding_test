"""
최대 그림의 넓이 update
그림의 갯수 count

현재 좌표에서 상하좌우 이동값이 1이면 그림 
더이상 1이 없다면 종료 

"""
from collections import deque

def bfs(start_x,start_y):
    #면적, 방문기록 업데이트
    visited[start_x][start_y]=True
    area=1

    q=deque([(start_x,start_y)])
    
    #q가 빌때까지 상하좌우 탐색
    while q:
        x,y=q.popleft()
        
        for dx,dy in d:
            nx=x+dx
            ny=y+dy

            if 0<=nx<r and 0<=ny<c and not visited[nx][ny]:
                if graph[nx][ny]=='1' : #그림일 경우 
                    visited[nx][ny]=True
                    #그림의 넓이 갱신
                    q.append((nx,ny))
                    area+=1
    return area
                


r,c=map(int,input().split())
graph=[list(input().split()) for _ in range(r)]
visited=[[False]*c for _ in range(r)]
d=[(1,0),(-1,0),(0,1),(0,-1)]

count=0
max_area=0

# 모든 좌표 탐색
for i in range(r):
    for j in range(c):
        if graph[i][j]=='1' and not visited[i][j]:
            count+=1
            max_area=max(max_area,bfs(i,j))

print(count)
print(max_area)

