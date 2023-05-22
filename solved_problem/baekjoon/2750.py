import sys
sys.stdin=open('baekjoon/input.txt','r')

n=int(input())
arr=sorted([int(input()) for _ in range(n)])

for x in arr:
    print(x)