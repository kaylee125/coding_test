
"""

풀이 방법
카펫에서 갈색 면적, 황색 면적 구하는 방법
- 황색면적=n*m
- 갈색면적=2n*2m+4 = 2(n*m)+4
- 위 공식대로 n과 m의 곱셈 결과가 yello의 갯수

제약 조건
- 가로길이는 세로길이보다 같거나 길다.


"""
def solution(brown, yellow):
    answer = []
    range_num=int((brown-4)/2)
    for x in range(range_num):
        if x*(range_num-x)==yellow:
            answer.append(x+2) #가로
            answer.append(range_num-x+2) #세로
            break
    answer.sort(reverse=True)
    return answer

def solution2(brown,yellow):
    """
    1.
    xy=yellow면적
    (x+2)(y+2)-xy=brown면적
    
    2.
    2x+2y+4=brown면적

    3.x>=y
    """
    answer=[]

    x=0
    y=0

    for i in range(1,yellow+1):
        if yellow%i==0:
            #xy=yellow면적
            x=i
            y=yellow//i
            if 2*x+2*y+4==brown:
                answer.append(x+2)
                answer.append(y+2)
                break
    answer.sort(reverse=True)
    return answer


print(solution2(24,24))