import sys
sys.stdin=open('baekjoon/input.txt','r')

scores={'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,
        'D+':1.5,'D0':1.0,'F':0.0}
cnt=0
sc=0
for _ in range(20):
    clss=list(map(str,input().split()))
    if clss[2]=='P':
        pass
    else:
        cnt+=float(clss[1])
        sc+=float(clss[1])*scores[clss[2]]

print(round(float(sc/cnt),6))
    