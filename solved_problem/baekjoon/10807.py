import sys
sys.stdin=open('baekjoon/input.txt','r')

n= int(input())
arr=list((map(int,input().split())))

print(arr)
max_val=max(arr)
min_val=min(arr)
print(min_val,max_val)