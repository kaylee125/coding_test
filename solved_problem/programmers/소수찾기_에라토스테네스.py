import math

#2부터 n까지의 모든 수에 대하여 소수 판별
def solution(n):
    answer=0

    #처음엔 모든 수가 소수인 것으로 초기화(0과 1 제외)
    array=[True for i in range(n+1)]

    #######에라토스테네스의 체 알고리즘 수행########
    #2부터 n의 제곱근까지의 모든 수를 확인하며
    for i in range(2,int(math.sqrt(n)+1)):
        if array[i]==True: #i가 소수인 경우(남은 수의 경우)
            #i를 제외한 i의 모든 배수를 지우기
             for j in range(i+i, n+1, i): # i이후 i의 배수들을 False 판정
                array[j] = False

    #모든 소수 출력
    for i in range(2, n+1):
        if(array[i] == True):
            answer += 1
    return answer

   
print(solution(5))

