import sys
sys.stdin=open('baekjoon/input.txt','r')

a,b,v=map(int,input().split())
h=0
day=0
while True:
    #하루동안 올라간 높이
    #낮
    day+=1
    h+=a
    if h>=v:
        break
    #밤
    h-=b
print(day)

