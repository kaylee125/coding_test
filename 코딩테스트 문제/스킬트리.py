def solution(skill, skill_trees):
    answer = -1
    new_trees=[]
    cnt=0
    for tree in skill_trees:
        word=''
        for s in tree:
            if s in skill:
                word+=s
        new_trees.append(word)

    for i in new_trees:
        if i in skill and skill.startswith(i):
            cnt+=1
            


        


    return cnt

print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]))