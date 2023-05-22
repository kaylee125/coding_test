import sys
sys.stdin=open('baekjoon/input.txt','r')
n=int(sys.stdin.readline())
boy_card=list(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())
cards=list(map(int,sys.stdin.readline().split()))
res=[0]*m
for i in range(len(cards)):
    if cards[i] in boy_card:
        res[i]=1
for x in res:
    print(x,end=' ')

