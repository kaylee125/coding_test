def solution(tasks):
    answer = 0
    daily=0
    for s,e,w in tasks:
        try: 
            daily=w//(e-s+1)
        except:
            daily=0
        print(daily)    
        
    return answer


solution([[0,1,4],[1,3,7],[2,2,3],[3,4,5]])