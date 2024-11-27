

N=int(input())
cache=[0]*(1000000+1)
cache[2]=1


def count_bottom_up(N):

    if N==2:
        return 1
    
    for n in range(3,N+1):
        
        if n%3==0 and n%2==0:
            cache[n]=min(cache[n//3]+1,cache[n//2]+1)
        elif n%3==0:
            cache[n]=min(cache[n//3]+1,cache[n-1]+1)
        elif n%2==0:
            cache[n]=min(cache[n//2]+1,cache[n-1]+1)
        else:
            cache[n]=cache[n-1]+1
    return cache[N]
        
print(count_bottom_up(N))


def count_top_down(n):

    if cache[n]>0:
        return cache[n]
    
    if n%3==0 and n%2==0:
        cache[n]=min(count_top_down(n//3)+1,count_top_down(n//2)+1)

    elif n%3==0:
        cache[n]=min(count_top_down(n//3)+1,count_top_down(n-1)+1)

    elif n%2==0:
        cache[n]=min(count_top_down(n//2)+1,count_top_down(n-1)+1)
    else:
        cache[n]=count_top_down(n-1)+1
            
    return cache[n]


print(count_top_down(N))