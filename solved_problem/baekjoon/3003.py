# 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개
import sys
chess=[1,1,2,2,2,8]
arr=[0]*6
given=list(map(int,input().split()))

for i,s in enumerate(given):
    if s>chess[i]: #체스판의 갯수보다 더 큰 경우 ->제거해야함
        arr[i]=-(s-chess[i])
    elif s<chess[i]:
        arr[i]=chess[i]-s
    else:
        arr[i]=0
for x in arr:
    print(x,end=' ')