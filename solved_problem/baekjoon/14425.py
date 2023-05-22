import sys
sys.stdin=open('baekjoon/input.txt','r')
n,m=map(int,input().split())
set_n=[sys.stdin.readline().rstrip() for _ in range(n)]
words=[sys.stdin.readline().rstrip() for _ in range(m)]
cnt=0
for word in words:
    if word in set_n:
        cnt+=1
print(cnt)