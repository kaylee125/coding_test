import datetime

def solution(today, terms, privacies):
    answer = []
    #유효기간 딕셔너리로 만듦
    term_dict=dict()
    res=[0]*len(privacies)

    for x in terms:
        a,b=(x.split(' '))
        term_dict[a]=int(b)
    
    t_year,t_mon,t_day=map(int,today.split('.'))
    
    for i in range(len(privacies)):
        date,typ=privacies[i].split(' ')
        year,mon,day=map(int,date.split('.'))
        
        if mon+term_dict[typ]>12:
            year+=1
            mon=(mon+term_dict[typ])-12
            day-=1

        else:
            mon+=term_dict[typ]
            day-=1

        print(year,mon,day)
        #유효기간 만료 판별
        if year<t_year:
            res[i]=1
        elif mon<t_mon:
            res[i]=1
        elif day<t_day:
            res[i]=1
        else:
            pass

    for i in range(len(res)):
        if res[i]==1:
            answer.append(i+1)
    
    return answer

print(solution("2022.05.19",["A 6", "B 12", "C 3"],
["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
# print(solution("2020.01.01",["Z 3", "D 5"],["2019.01.01 D", "2019.11.15 Z", 
# "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))