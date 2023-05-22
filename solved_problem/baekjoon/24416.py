import sys
sys.stdin=open('input.txt','r')

def recur_dp(n):#top down방식 위에서부터 재귀호출 
    if n==1 or n==2:
        return 1
    else:
        fib=recur_dp(n-1)+recur_dp(n-2)
        return fib

def bottom_up_dp(n): #bottom up 방식 

    fib=[0]*(n+1)
    fib[1]=1
    fib[2]=1
    cnt=0

    for i in range(3,n+1):
        cnt+=1
        fib.append(fib[i-1]+fib[i-2])
    return cnt

if __name__=='__main__':
    n=int(input())
    print(recur_dp(n),end=' ')
    print(bottom_up_dp(n))
