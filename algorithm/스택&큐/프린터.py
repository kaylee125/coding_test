from collections import deque
def solution(priorities, location):
    q=deque(priorities)
    answer=0
    while priorities:
        priorities[location]
        a=q.popleft()
        if a<max(priorities):
            q.append(a)
        else:
            answer+=1
            print(priorities[location])
            # if priorities[location]==a:
            return answer


print(solution([1, 1, 9, 1, 1, 1],0))