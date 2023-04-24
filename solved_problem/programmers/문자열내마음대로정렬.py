def solution(strings, n):

    #n번째 문자를 기준으로 sort하겠다는 key값을 설정해준다
    answer=sorted(sorted(strings),key=(lambda x:x[n]))
    
    return answer

print(solution(["sun", "bed", "car"],1))

"""
1.sorted(정렬할 데이터,key파라미터)
key파라미터:어떤 것을 기준으로 정렬할 것인가? 에 대한 기준
2.람다함수 
lambda: (매개변수:표현식)

ex.두수를 더하는 함수를 람다로 작성
(lambda x,y:x+y)(10,20)

"""