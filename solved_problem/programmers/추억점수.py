
def solution(name, yearning, photo):
    answer = []
    yearning_score=0
    #딕셔너리 만들기
    dic={key:value for key,value in zip(name,yearning)}
    # dic=dict(zip(name,yearning))
    
    for p in photo:
        
        for person in p:
            if person in dic:
                yearning_score+=dic[person]
        answer.append(yearning_score)
        yearning_score=0
    
    return answer


name=["may", "kein", "kain", "radi"]
yearning=[5, 10, 1, 3]
photo=[["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
print(solution(name,yearning,photo))