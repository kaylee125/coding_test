import sys
sys.stdin=open('baekjoon/input.txt','r')
n=int(input())
s=input()
total=0
for x in s:
    total+=int(x)

print(total)