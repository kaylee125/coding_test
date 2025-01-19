""""
도영이는 짜파구리 요리사로 명성을 날렸었다. 이번에는 이전에 없었던 새로운 요리에 도전을 해보려고 한다.

지금 도영이의 앞에는 재료가 N개 있다. 도영이는 각 재료의 신맛 S와 쓴맛 B를 알고 있다. 여러 재료를 이용해서 요리할 때, 그 음식의 신맛은 사용한 재료의 신맛의 곱이고, 쓴맛은 합이다.

시거나 쓴 음식을 좋아하는 사람은 많지 않다. 도영이는 재료를 적절히 섞어서 요리의 신맛과 쓴맛의 차이를 작게 만들려고 한다. 또, 물을 요리라고 할 수는 없기 때문에, 재료는 적어도 하나 사용해야 한다.

재료의 신맛과 쓴맛이 주어졌을 때, 신맛과 쓴맛의 차이가 가장 작은 요리를 만드는 프로그램을 작성하시오.
"""

def recur(idx,sour,bitter,use_cnt):
    """
    N depth까지 재귀실행

    """
    global answer
    if idx==N:
        if use_cnt==0:
            return
        result=abs(sour-bitter)
        answer=min(answer,result)
        return 

    #재료 추가할 경우와 재료 추가하지 않을 경우 신맛은 곱해지고 쓴맛은 더해짐

    #추가할 경우
    recur(idx+1,sour*ingred[idx][0],bitter+ingred[idx][1],use_cnt+1)

    #추가하지 않을 경우 
    recur(idx+1,sour,bitter,use_cnt)
    

N=int(input())
ingred=[list(map(int,input().split())) for _ in range(N)]
answer=9999999999

recur(0,1,0,0)
print(answer)
