
## top down -> 재귀
## bottom up ->반복문

n=int(input())
cache=[ -1 for _ in range(91)]
cache[0]=0
cache[1]=1

def p(n):

    if cache[n]==-1: #처음 구하는 경우 
        cache[n]= p(n-1)+p(n-2)

    return cache[n]

print(p(n))

