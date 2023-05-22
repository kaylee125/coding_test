n=int(input())
ans=''
for i in range(n-1,-1,-1):
    ans=' '*i+'*'*(n-i)
    print(ans)
    

