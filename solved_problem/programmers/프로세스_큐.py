from collections import deque
def solution(priorities, location):
    answer = 0
    my_doc = [0 for _ in range(len(priorities))] #[0,0,0,0]
    my_doc[location] = 1 # location=2 mydoc ->[0,0,1,0]
    queue = deque(priorities)
    
    while True:
        if not my_doc or max(my_doc) == 0:
            print('Break!')
            break

        if max(queue) == queue[0]: #우선순위가 가장 높은 경우 ->큐에서 삭제하고 
            queue.popleft() 
            del my_doc[0]
            answer += 1 #실행프로세스+1
        else:
            queue.append(queue[0]) #큐의 마지막으로 다시 append
            my_doc.append(my_doc[0])
            queue.popleft() #앞에꺼는 삭제
            del my_doc[0]


    return answer

            
print(solution([2, 1, 3, 2],2))
# print(solution([1, 1, 9, 1, 1, 1],0))