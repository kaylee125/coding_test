import sys
sys.stdin=open('baekjoon/input.txt','r')

n,k=map(int,input().split())
arr=list(map(int,input().split()))
print(sorted(arr,reverse=True)[k-1])
