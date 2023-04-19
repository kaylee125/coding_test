def recursion(n,i,limit):
    if n==limit:
        return True
    if n>limit:
        return False
    n+=i
    return recursion(n,i+1,limit)

def solution(n):
    answer=0
    for i in range(1,n+1):
        if recursion(i,i+1,n):
            answer+=1
    return answer

print(solution(15))