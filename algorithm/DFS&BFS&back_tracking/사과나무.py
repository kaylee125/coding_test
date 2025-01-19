'''
- 출발지점: 격자의 중심
- 2차원 배열의 중심에서 시작하여 레벨(L)이 되기 n//2전 까지 탐색을 하면 
마름모 모양으로 퍼진다

자료구조
- 방문여부 check용 이차배열:방문했으면 1 안했으면 0
- 입력받은 2차배열:각 원소는 수확할 사과의 개수



'''
import sys
from collections import deque
sys.stdin=open("section7/8. 사과나무/in1.txt",'r')

n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
chk=[[0]*n for _ in range(n)]
sum=0
dx=[-1,1,0,0]
dy=[0,0,-1,1]
Q=deque()
#출발지점에서의 수확한 사과의 개수
sum+=a[n//2][n//2]
chk[n//2][n//2]=1
Q.append((n//2,n//2)) #중앙점에서 탐색 시작
L=0
while Q:
    if L==n//2:
        break
    else:
        size=len(Q)
        for i in range(size):
            tmp=Q.popleft()
            for j in range(4):
               x=tmp[0]+dx[j]
               y=tmp[1]+dy[j]
               if chk[x][y]==0:
                   sum+=a[x][y]
                   chk[x][y]=1
                   Q.append((x,y))
        L+=1
print(sum)
