import sys
sys.stdin=open('baekjoon/input.txt','r')
n,m=map(int,sys.stdin.readline().split())
N=[sys.stdin.readline().rstrip() for _ in range(n)]
res=[]
for _ in range(m):
    x=sys.stdin.readline().rstrip()
    if x in N:
        res.append(x)
print(len(res))
for x in res.sort():
    print(x)