import sys
sys.stdin=open('baekjoon/input.txt','r')
n=int(input())
arr=[sys.stdin.readline().split() for _ in range(n)]
names={}

for name,info in arr:
    if info=='leave':
        names[name]=1
    if info=='enter':
        names[name]=0
#사전 순의 역순으로 한 줄에 한 명씩 출력
ans=[]
for name in names:
    if names[name]==0:
        ans.append(name)
ans.sort(reverse=True)
for x in ans:
    print (x)
