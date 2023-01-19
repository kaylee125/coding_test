def solution(id_list, report, k):
    
    # 한줄코드: rep_dict={id:[] for id in id_list}
    rep_dict=dict()
    for id in id_list:
        rep_dict[id]=[]
    
    #유저 id별로 처리메일받을 횟수를 저장할 값
    answer = [0] * len(id_list)  #[0, 0, 0, 0]

    for x in set(report):#set사용으로 중복 제거함
        rep=x.split()
        #key:신고받은 사람 value:신고한 사람
        rep_dict[rep[1]].append(rep[0]) #rep_dict[rep[1]]은 객체가 리스트이므로 append()가능
    
    
    #k번 이상 신고->딕셔너리 value의 길이를 보면 몇번 신고당했는지 알 수 있음
    for key,value in rep_dict.items():
        if len(value)>=k:#신고한 사람이 k명 이상이면
            for v in value:
                answer[id_list.index(v)]+=1 #각 신고ID별 인덱스번호로 접근하여 1씩 증가시키기
    return answer            
print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))