"""
N길이의 배열을 false로 초기화 후 방문할때마다 체크
무방향 그래프==양방향그래프 
"""

N,M=map(int,input().split())
#인접행렬 생성
adj=[[0]*N for _ in range(N)]

#인접행렬에 값 삽입
for _ in range(M):
    a,b=map(int,input().split())
    a-=1
    b-=1
    adj[a][b]=a[b][a]=1

ans=0 #연결요소갯수
chk=[False]*N #방문 체크배열

def dfs(now):
    for nxt in range(N):
        if adj[now][nxt] and not chk[nxt]: #not chk[nxt] ->한번 방문한 곳은 다시 방문 안함
            chk[nxt]=True
            dfs(nxt)

for i in range(N):
    if not chk[i]:
        ans+=1
        chk[i]=True
        dfs(i)