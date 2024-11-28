N=int(input())

#S의 모든 소인수가 106보다 크다면 그 수는 적절한 암호 키이고, 그렇지 않은 경우는 적절하지 못한 암호 키가 된다.
#하나라도 10의 6승 보다 작은 소인수가 있다면 no 그 외는 yes
for _ in range(N):
    s=int(input())
    for i in range(2,1000001):
        if s%i==0:
            print('NO')
            break
        if i==1000000:
            print('YES')

        
        

        
