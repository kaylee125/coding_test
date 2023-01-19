from collections import deque
def solution(progresses, speeds):
    answer=[]
    prog=[]
    ans=0
    
    # (배포우선순위:작업개수)로 queue
    for a,b in enumerate(progresses):
        prog.append((a+1,b))
    q=deque(prog) #deque([(1, 93), (2, 30), (3, 55)])

#작업개수와 작업속도를 순차적으로 더한다
#작업률이 100인게 확인되면 해당 튜플의 [0]번째 원소가 q원소 중 가장 큰 값인지 확인 ==max(q)
#가장 큰값이면 배포->누적값+1한걸 return 
#가장 큰 값이 아니면 누적값으로 저장

    while q:
        for i in range(len(speeds)):
            a=q[i][1]+speeds[i]
            if a==100 and q[i][0]==max(q):
                answer.append(ans+1)
                q.popleft()#작업 끝났으면
            else:
                ans+=1




print(solution([93, 30, 55],[1, 30, 5]))