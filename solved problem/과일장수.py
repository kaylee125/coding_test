def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    add_min=0 
    split_list=[]

    #사과를 m개의 상자로 나누어 담기(리스트 분할)
    for i in range(0,len(score),m): #0 부터 배열의 최대길이까지 n 개 씩 증가
        split_list.append(score[i:i+m])

    #각 박스별 최저 사과점수 산출
    for i in split_list:
        if len(i)==m:#조건:상자단위로 판매하기 때문에 나머지는 버린다.
            add_min+=min(i) #모든 상자에 담긴 최저 사과점수를 누적합
    
    answer=add_min*m
    
    return answer

# print(solution(4,3,[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))
print(solution(3,4,[1, 2, 3, 1, 2, 3, 1]))