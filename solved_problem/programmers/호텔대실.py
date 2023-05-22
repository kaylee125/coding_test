'''
최소한의 객실 사용
퇴실시간 기준 10분간 청소 후 다음 손님 이용 가능
필요한 최소객실의 수 return
힙으로 풀어보기..
'''

def solution(book_time):
    answer = 0
    book_time.sort(key=lambda x:x[0])
    
    for time in book_time:
        if time[1]+10 
    return answer

book_time=[["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]
print(solution(book_time))
