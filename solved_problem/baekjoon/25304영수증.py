import sys
sys.stdin=open('/Users/leesh970930/Desktop/coding_algorithm/solved_problem/baekjoon/input.txt','r')

total=int(input())
n=int(input())
for _ in range(n):
    price,quantity=map(int,input().split())
    total-=price*quantity

if total==0:
    print('Yes')
else:
    print('No')


