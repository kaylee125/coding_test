import sys
sys.stdin=open('baekjoon/input.txt','r')
num='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n,b=map(int,input().split())
#몫,나머지=divmod(n,b)
res=''
while n>0:
    n,rest=divmod(n,b)
    res+=num[rest]

res=''.join(reversed(res))
print(res)