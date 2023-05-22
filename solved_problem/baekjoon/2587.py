import sys
sys.stdin=open('baekjoon/input.txt','r')

arr=sorted([int(input())for _ in range(5)])
print(round(sum(arr)/5))
print(arr[2])