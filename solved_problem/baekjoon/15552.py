import sys
sys.stdin=open('baekjoon/input.txt','r')

n=int(sys.stdin.readline())
for i in range(1,n+1):
    a,b=map(int,sys.stdin.readline().split())
    print('Case #%d: %d + %d = %d'% (i,a,b,a+b))
