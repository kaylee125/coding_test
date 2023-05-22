from queue import PriorityQueue

def solution(priorities, location):
    q=PriorityQueue()
    for idx,priority in enumerate(priorities):
        print(priority,idx)
        q.put((priority,idx))
    print(q.get()[1])
    return 0


print(solution([2, 1, 3, 2],2))