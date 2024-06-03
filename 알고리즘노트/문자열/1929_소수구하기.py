"""
소수 구할때는 에라토스테네스의 체!!
1)1은 소수 아님
2)2~n까지 소수인지 아닌지 검사
3)n이 소수인지 검사할때:2~n-1까지 n으로 나눴을때 나머지가 0이 아닌 수는 소수로 판별"""

M,N= map(int,input().split())

for n in range(M,N+1):
    if n<2:
        continue
    
    for x in range(2,int(n**0.5)+1):
        if n%x==0:#0으로 나누어 떨어지는게 한개라도 있으면 소수 아님
            break
    else:
        print(n)
        
    
        
    

