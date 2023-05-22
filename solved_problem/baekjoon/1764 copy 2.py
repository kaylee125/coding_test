import sys
sys.stdin=open('baekjoon/input.txt','r')
n,m=map(int,sys.stdin.readline().split())
N={}

for _ in range(n):
    x=sys.stdin.readline().rstrip()
    N[x]=0

for _ in range(m):
    x=sys.stdin.readline().rstrip()
    try:
        if x in N:
            N[x]=1
    except:
        pass
res=[]
for k,v in N.items():
    if v==1:
        res.append(k)
res.sort()
print(len(res))
for x in res:
    print(x)