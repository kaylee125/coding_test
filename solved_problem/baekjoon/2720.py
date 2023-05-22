import sys
sys.stdin=open('baekjoon/input.txt','r')

T=int(input())


for _ in range(T):
    m=int(input())
    res=[0,0,0,0]
    while True:

        if m>=25:
            res[0]=m//25
            m=m%25
        elif m>=10:
            res[1]=m//10
            m=m%10
        elif m>=5:
            res[2]=m//5
            m=m%5
        else:
            res[3]=m
            break
    for x in res:
        print(x,end=' ')
    print()
