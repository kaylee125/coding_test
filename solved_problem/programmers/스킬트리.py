def solution(skill, skill_trees):
    answer = -1
    new_trees=[]
    cnt=0

    #skill_trees 각 원소에서 skill에 해당하지 않는 문자 제거 한 값을 새로운 리스트(new_trees)에 추가
    for tree in skill_trees:
        word=''
        for s in tree:
            if s in skill:
                word+=s
        if skill.startswith(word):
            cnt+=1
    return cnt



print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]))
'''
<다른사람 풀이>
def solution(skill,skill_tree):
    answer=0
    for i in skill_tree:
        skillist=''
        for z in i:
            if z in skill:
                skillist+=z
        if skillist==skill[0:len(skillist)]:
            answer+=1
    return answer

    '''

print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]))