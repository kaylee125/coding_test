import heapq as hq

def solution(scoville, K):
    answer = 0
    a=[]

    for s in scoville:
        hq.heappush(a,s)

    print(min(a))
    while True:
        if min(a)>7:
            break
        
        new=a[0]+a[1]*2
        if a[0]<7 and new>7:
            a.pop(0)
        if a[1]<7 and new>7:
            a.pop(0)
        a.append(new)
        

    print(a)
    return answer

print(solution([1, 2, 3, 9, 10, 12],7))