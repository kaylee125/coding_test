#트럭 여러대가 일차선 다리를 순서대로 건넘
#모든 대기 트럭이 다리를 건너려면 몇초가 걸리는지?
#다리에 올라갈 수 있는 트럭의 최대 갯수와 무게가 존재한다
#다리에 완전히 오르지 않은 트럭의 무게는 무시한다.

#시간초과 해결을 위해 큐로 변경해서 다시 풀어보기
from collections import deque

def solution(bridge_length,weight,truck_weights):
    #다리 위를 리스트로 추상화
    bridge=[0]*bridge_length
    

    while True:
        if len(truck_weights)==0 and sum(bridge)==0:
            break

        time+=1
        bridge.pop(0)#맨 앞에 원소를 팝 해야하기 때문에 pop(0)을 해줌
        if truck_weights:
            if sum(bridge)+truck_weights[0]<=weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
    return time

print(solution(2,10,[7,4,5,6]))