
def solution(d, budget):
    answer = 0
    d=sorted(d)
    
    for i in d:
        if budget<i:
            return answer
        budget-=i
        answer+=1
    return answer

    '''<다른코드>
        for i in d :
            budget -= i
            if budget < 0 :
                break
            cnt += 1
        answer = cnt
        return answer    
    '''
print(solution([1,3,2,5,4],9))
print(solution([2,2,3,3],10))