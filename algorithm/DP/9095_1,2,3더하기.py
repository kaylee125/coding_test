 

T=int(input())

for _ in range(T):
    n=int(input())

    cache=[0]*12
    cache[1]=1
    cache[2]=2
    cache[3]=4

    for i in range(4,n+1):
        
        cache[i]=cache[i-1]+cache[i-2]+cache[i-3]
    print(cache[n])
