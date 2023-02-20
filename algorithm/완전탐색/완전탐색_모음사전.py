'''
1.아이디어
DFS 재귀로 풀자.


2.시간복잡도
3.자료구조
'''

def DFS(L):
    if L==5:
        print(res)
    else:
        for i in range(len(moem)):
            res+=moem[i]
            DFS(L+1)

            
def solution(word):
    res=""
    moem=['A', 'E', 'I', 'O', 'U']
    answer = 0
    return answer

print(solution("AAAAE"))