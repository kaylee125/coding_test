import sys
sys.stdin=open('baekjoon/input.txt','r')
n,m=map(int,sys.stdin.readline().split())
N=[sys.stdin.readline().rstrip() for _ in range(n)]
M=[sys.stdin.readline().rstrip() for _ in range(m)]
res=[]
if n>m:
    for x in M:
        if x in N:
            res.append(x)
else:
    for x in N:
        if x in M:
            res.append(x)
    
res.sort()
print(len(res))
for x in res:
    print(x)