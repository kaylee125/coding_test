from collections import deque

N,M=map(int,input().split())
board=[input() for _ in range(N)]

# 방문체크
# chk=[[False]*M for _ in range(N)]

#상하좌우 좌표
dy=(0,1,0,-1)
dx=(1,0,-1,0)

#유효한 좌표인지 검사
def is_valid(y,x):
    return 0<=y<N and 0<=x<M


def bfs():
    chk=[[False]*M for _ in range(N)]
    chk[0][0]=True
    q=deque()
    q.append((0,0,1)) #첫번째 좌표 y,x,cnt

    while q:
        y,x,d=q.popleft()

        if y==N-1 and x==M-1:
            return d
        nd=d+1 #도착점에서의 칸수 출력 후 +1

        for i in range(4):
            #상하좌우 방문하면서 유효한 좌표 q에 추가
            ny=y+dy[i]
            nx=x+dx[i]
            if is_valid(ny,nx) and not chk[ny][nx] and board[ny][nx]=='1':
                chk[ny][nx]=True
                q.append((ny,nx,nd))
        
print(bfs())