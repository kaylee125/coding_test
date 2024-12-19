import sys
import os
print("Current Working Directory:", os.getcwd())

sys.stdin = open('/Users/sunny/Desktop/coding_test/algorithm/DP/input.txt', 'r')

n=int(input())
squares=[0]*1001

#튜플로 인풋받아서 x축 기준 정랼하기
#가장 높은 기둥의 값 변수로 저장
max_y=0
max_x=0
for i in range(n):
    x,y=map(int,input().split())
    squares[x]=y
    if max_y<y:
        max_x=x
        max_y=y

ans=0
curr=0
# #왼쪽~ 최대기둥까지
for i in range(max_x+1):
    #현재 좌표까지 가장 높은 인덱스
    curr=max(squares[i],curr)
    ans+=curr

curr=0
for i in range(1000,max_x,-1):
    curr=max(squares[i],curr)
    ans+=curr
print(ans)

