
#n이 0일때 피보나치수는 0 1일때는 1
def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

if __name__ == '__main__':
    n=int(input())
    result=0
    print(fibo(n))
