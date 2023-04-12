#정답을 찍는 규칙성
def solution(answers):

    a=[1,2,3,4,5]*2000
    b=[2,1,2,3,2,4,2,5]*2000
    c=[3,3,1,1,2,2,4,4,5,5]*2000

    aa={
        1:0,
        2:0,
        3:0
    }  

    result=[] 
    
    # 맞춘 문제 갯수 세기
    for x in range(len(answers)):
        if answers[x]==a[x]:
            aa[1]+=1
        if answers[x]==b[x]:
            aa[2]+=1
        if answers[x]==c[x]:
            aa[3]+=1
    
    #딕셔너리 value의 최대값과 값 벨류값을 비교하여 동일하면 result로 append
    for i in range(1,4):
        if aa[i]==max(aa.values()):
            result.append(i)

    return sorted(result)

print(solution([1,3,2,4,2]))
# print(solution([1,2,3,4,5]))


'''
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
    
    '''