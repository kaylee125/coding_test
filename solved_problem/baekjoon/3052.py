import sys
sys.stdin=open('baekjoon/input.txt','r')

ans=set()
for _ in range(10):
    i=int(input())%42
    ans.add(i)
print(len(ans))

