import sys
sys.stdin=open('baekjoon/input.txt','r')

T=int(input())
for _ in range(T):
    r,s=map(str,input().split())
    print(''.join(x*int(r) for x in s))

