import sys 

base='/Users/leesh970930/Desktop/pythonalgorithm_formac/섹션 4/'
sys.stdin=open(base+'1. 이분검색/in1.txt', "r")

n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
#이분검색할때 lt,rt,mid값 필요(투포인터)
lt=0
rt=n-1

while lt<=rt:
    mid=(lt+rt)//2
    
    if a[mid]==m:
        print(mid+1)
        break
    elif a[mid]>m:
        rt=mid-1
    else:
        lt=mid+1

