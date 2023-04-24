def solution(a, b, n):
    answer = 0
    coke=0
    while True :
        
        #교환 가능한 콜라의 개수
        coke=b*(n//a)
        #현재 보유중인 콜라병의 개수
        n=coke+(n%a)
        answer+=coke

        #만약 교환 가능한 콜라의 개수가 없으면 멈춤
        if coke==0:
            break
    return answer

#잘한 풀이 예
def solution2(a, b, n):
    answer = 0
    while n >= a: #돌려받을 빈병이 있을때까지
        answer += (n // a) * b
        n = (n // a) * b + (n % a)
    return answer

print(solution(2,1,20))
print(solution2(2,1,20))