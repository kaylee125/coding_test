def solution(s):
    answer = ''
    tmp=[]
    # words=list(map(str,s.split(' ')))
    words=s.split(' ')
    print(words)
    for word in words:
        word=word.capitalize()
        tmp.append(word)
    return ' '.join(tmp)

print(solution("3people   unFollowed me"))