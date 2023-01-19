from collections import deque
def solution(priorities, location):
    pridict={i:priorities[i] for i in range(len(priorities))}
    answer=0
    
    while priorities:
        answer+=1
        pridict.popitem(0)
        print(pridict)
        # if pridict.get(location)==a:
        #     return answer
        #     break

    #pridict가
    # q=deque(priorities)
    # answer=0
    # while priorities:
        
    #     a=q.popleft()
    #     if a<max(priorities):
    #         q.append(a)
    #     else:
    #         answer+=1
    #         print(priorities[location])
    #         # if priorities[location]==a:
    #         return answer


print(solution([1, 5, 9, 1, 1, 1],0))