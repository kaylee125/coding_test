T=int(input())


def count(n,cache):

    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    
    if cache[n] !=0:
        return cache[n]
    
    cache[n]=count(n-1,cache)+count(n-2,cache)+count(n-3,cache)
    return cache[n]
    

    #값이 있을 경우 
for _ in range(T):
    n=int(input())

    cache=[0]*12

    print(count(n,cache))

