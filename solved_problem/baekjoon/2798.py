import sys
sys.stdin=open('baekjoon/input.txt','r')

n,m=map(int,input().split())
card=list(map(int,input().split()))
max=0
for i in range(1,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            hap=card[i]+card[j]+card[k]
            if hap<=m:
                if hap>max:
                    max=hap
            
            
print(max)