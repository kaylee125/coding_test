
'''
h-index 구하는 방법: 논문이 많이 인용된 순으로 정렬한 후 피인용수가 논문수와 같아지거나 
피인용수가 논문수보다 작아지기 시작하는 숫자

'''
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0
    

print(solution([3, 0, 6, 1, 5]))