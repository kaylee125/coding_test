import sys
sys.stdin=open('baekjoon/input.txt','r')

n=int(input())
arr=list(map(int,input().split()))
m=max(arr)

total=0
for score in arr:
    total+=float(score/m*100)
print(total/len(arr))