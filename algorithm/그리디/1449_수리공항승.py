N,L=map(int,input().split())
coordi=[False]*1001

for i in map(int,input().split()):
    coordi[i]=True

ans=0
x=0

while x<1001:
    if coordi[x]:
        x+=L
        ans+=1
    else:
        x+=1

## 좌표압축으로 푸는 방법 ->공간복잡도를 줄일 수 있음, 좌표범위가 매우 클 때 유용

