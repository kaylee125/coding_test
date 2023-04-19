#스스로 품
def solution(n):
    answer = 0
    n_cnt=0
    n_b=format(n,'b')
    for i in list(n_b):
        if i=='1':
            n_cnt+=1
    
    for i in range(n+1,1000000):
        a=format(i,'b')
    
        cnt=0
        for j in list(a):
            if j=='1':
                cnt+=1
        if n_cnt==cnt:
            return i
            
print(solution(78))