def solution(numbers):
    #numbers 모든 원소를 문자열로 변경
    numbers=list(map(str,numbers))
    #문제 조건에서 주어진 자연수의 자릿수는 1000 이하 값이기 때문에 정렬조건 key값으로 문자열로 변환한 각 원소에 *3을 한 후 
    #내림차순 정렬을 수행한다.
    numbers.sort(key=lambda x:x*3,reverse=True)
    return str(int(''.join(numbers)))
    print(numbers)




print(solution([6, 10, 2]))

'''
시간초과오류 ㅠㅠㅠ
from itertools import permutations

def solution(numbers):

    a=[]
    arr=list(permutations(numbers))

    for x in arr:
        answer = ''
        for s in x:
            answer+=str(s)
        a.append(answer)  
    return max(a)
'''

