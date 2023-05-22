import sys
sys.stdin=open('baekjoon/input.txt','r')
T=int(input())
for _ in range(T):
    score=list(map(int,input().split()))
    n=score.pop(0)
    avg=sum(score)/n
    cnt=0
    for i in score:
        if avg<i:
            cnt+=1
    res=round((cnt/n)*100,3)

    print('%0.3f%%'%res)
