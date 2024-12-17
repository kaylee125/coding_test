import sys
import os
print("Current Working Directory:", os.getcwd())

sys.stdin = open('/Users/sunny/Desktop/coding_test/algorithm/DP/input.txt', 'r')

n=int(input())
squares=[]
dp_r=[]# x축의 오른쪽부터 시작했을때 x좌표(인덱스)별 창고높이 값 저장
dp_l=[]
#튜플로 인풋받아서 x축 기준 정랼하기
#가장 높은 기둥의 값 변수로 저장
max_y=0
max_x=0
for _ in range(n):
    x,y=map(int,input().split())
    squares.append((x,y))
    if max_y<y:
        max_x=x
        max_y=y



squares.sort(key=lambda x:x[0])
print(squares)
ans=0
curr=0
# #왼쪽~ 최대기둥까지
for i in range(max_x+1):
    #현재 좌표까지 가장 높은 인덱스
    max_y=max(squares[i][1],curr)
    ans+=max_y

# curr=0
# for i in range(len(squares),max_x,-1):
#     max_y=max(squares[i][1],curr)
#     ans+=max_y
print(ans)

