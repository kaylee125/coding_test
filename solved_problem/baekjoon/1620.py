'''N=도감에 수록되어 있는 포켓몬의 개수 
M=맞춰야 하는 문제의 개수

 문제가 알파벳으로만 들어오면 포켓몬 번호를 말해야 하고, 
 숫자로만 들어오면, 포켓몬 번호에 해당하는 문자를 출력'''

import sys
sys.stdin=open('baekjoon/input.txt','r')
n,m=map(int,sys.stdin.readline().split())
dic1={}
dic2={}
for i in range(1,n+1):
    name=sys.stdin.readline().rstrip()
    dic1[i]=name
    dic2[name]=i
for _ in range(m):
    q=sys.stdin.readline().rstrip()
    if q.isnumeric():
        print(dic1[int(q)])
    else:
        print(dic2[q])
