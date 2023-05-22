import sys
sys.stdin=open('baekjoon/input.txt','r')
num='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n,b=map(str,input().split())
n=n[::-1]
b=int(b)

res=0
for i in range(len(n)-1,-1,-1):
    res+=num.index(n[i])*(b**i)
    print(i,n[i],num.index(n[i]),b)

print(res)