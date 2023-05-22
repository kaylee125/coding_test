import sys
sys.stdin=open('baekjoon/input.txt','r')

n=int(sys.stdin.readline())
arr=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
arr=sorted(arr,key=lambda x:(x[1],x[0]))
for x,y in arr:
    print(x,y)

