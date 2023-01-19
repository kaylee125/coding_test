
from datetime import datetime,date

def solution(a, b):
    day=['SUN','MON','TUE','WED','THU','FRI','SAT']
    answer = ''
    month=1
    dat=1
    while month==a and dat==b:
        #month갱신
        month+=1
            #dat갱신
        if a==2:
            b>=1 and b<=28
        elif a in [1,3,5,7,8,10,12]:
            b>=1 and b<=31
        else:
            b>=1 and b<=30

    
    return answer

print(solution(5,24))