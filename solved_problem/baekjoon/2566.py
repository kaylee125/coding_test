#row 별로 max값과 인덱스를 찾고 반복문 돌며 업데이트

#입력받기
import sys
sys.stdin=open('baekjoon/input.txt','r')
arr=[list(map(int,input().split())) for _ in range(9)]
max=0
idx_i=0
idx_j=0

for i in range(9):
    for j in range(9):
        if arr[i][j]>max:
            max=arr[i][j]
            idx_i=i
            idx_j=j
print(max)
print(idx_i+1,idx_j+1)

        