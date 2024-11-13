from collections import deque
import math
def solution(progresses, speeds):
    answer = []
    q=deque(tuple(zip(progresses,speeds)))


    while q:
        #배포 초기화
        deploy=0

        #첫번째 작업을 끝내기 위해 남은 작업진도 계산 ->정수로 올림처리(작업진도는 정수단위이므로)
        days_needed=math.ceil((100-q[0][0])/q[0][1])

        # 각 작업의 진도 업데이트 (단 100 초과하지 않도록)
        q =deque([(min(p+days_needed*s,100), s) for p, s in q])

        #첫번째 작업이 완료되었다면 배포한 기능갯수만큼 증가 및 큐에서 제거
        while q and q[0][0]>=100:
            q.popleft()
            deploy+=1

        if deploy: 
            answer.append(deploy)
            
    return answer

progresses=[93, 30, 55]
speeds=	[1, 30, 5]
print(solution(progresses,speeds))