from collections import deque

def solution(progresses, speeds):
    answer = []
    q=deque(tuple(zip(progresses,speeds)))
    
    while q:
        #배포 초기화
        deploy=0

        #첫번째 작업이 완료되었다면 배포기능 갯수 증가 및 큐에서 제거
        while q and q[0][0]>=100:
            q.popleft()
            deploy+=1

        # 각 작업의 진도 증가
        q =deque([(p+s, s) for p, s in q])

        if deploy: 
            answer.append(deploy)
            
    return answer

progresses=[95, 90, 99, 99, 80, 99]
speeds=[1, 1, 1, 1, 1, 1]
solution(progresses,speeds)