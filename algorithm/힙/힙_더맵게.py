import heapq as hq

def solution(scoville, K):
    cnt=0
    
    a=[]
    for s in scoville:
        hq.heappush(a,s)

    while a[0]<K:
        try:
            cnt+=1
            new_scoville=hq.heappop(a)+hq.heappop(a)*2
            hq.heappush(a,new_scoville)
            
        except:
            return -1
    
    return cnt

    

print(solution([1, 2, 3, 9, 10, 12],7))