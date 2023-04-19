'''
1.문제설명: 입력된 날짜까지의 일수를 계산 한 뒤 7로 나눈 나머지 값으로 요일 판별
2.시간복잡도
3.자료구조:
    endofday:월별 일수 리스트
    요일별 리스트
'''

def solution(a, b):
    endofday=[0,31,29,31,30,31,30,31,31,30,31,30,31]
    day=['THU','FRI','SAT','SUN','MON','TUE','WED'] #금요일이 1번 인덱스에 위치하도록 요일 배열(1월 1일은 금요일)
    date=0

    for i in range(1,a):#a 직전 달 까지의 일수 구한 후 +b
        date+=endofday[i]
    date+=b
    answer=day[date%7]
    return answer

print(solution(5,24))

##datetime 모듈로