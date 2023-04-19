def solution(numbers, hand):
    answer = ''
    #키패드의 버튼을 각 좌표값으로 딕셔너리 생성
    d={1:[0,0],2:[0,1],3:[0,2],
        4:[1,0],5:[1,1],6:[1,2],
        7:[2,0],8:[2,1],9:[2,2],
        '*':[3,0],0:[3,1],'#':[3,2]}
    #왼손과 오른손의 start위치
    left_s=d['*']
    right_s=d['#']

    for n in numbers:
        #현재 좌표값
        now=d[n]
        if n in [1,4,7]:
            answer+='L'
            left_s=now #현재 좌표값은 왼손이 위치하고 있음
        elif n in [3,6,9]:
            answer+='R'
            right_s=now
        else:
            #2,5,8,0 누른 경우 현재위치와의 좌표 거리 계산해주기
            #현재 좌표값과 오른손,왼손의 위치와의 거리 각각 구하기
            left_d=0
            right_d=0
            for a,b,c in zip(left_s,right_s,now):
                left_d+=abs(a-c)
                right_d+=abs(b-c)

            if left_d>right_d:
                answer+='R'
                right_s=now
            elif left_d<right_d:
                answer+='L'
                left_s=now
            else:
                if hand=='right':
                    answer+='R'
                    right_s=now
                else:
                    answer+='L'
                    left_s=now

    return answer
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],'right'))