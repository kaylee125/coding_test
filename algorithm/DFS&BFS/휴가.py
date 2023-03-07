'''
부분집합 형태의 문제
(상담을 하느냐, 하지 않느냐)

'''
import sys 

# base='/Users/leesh970930/Desktop/pythonalgorithm_formac/섹션 7/'
sys.stdin=open('2. 휴가/in4.txt', "r")

def DFS(L,value):
    global max_val
    if L>n+1:
        return
    
    if L==n+1:
        if max_val<value:
            max_val=value
    else:
        #L일차에 상담 할 경우
        DFS(L+t[L],value+p[L])
        #안할 경우
        DFS(L+1,value)


if __name__=='__main__':
    n=int(input())
    t=[]#상담일수
    p=[]#금액
    max_val=0
    for _ in range(n):
        a,b=map(int,input().split())
        t.append(a)
        p.append(b)
    #index번호를 날짜로 보기 위한 시작하기 위한 작업
    t.insert(0,0)
    p.insert(0,0)
    DFS(1,0)
    print(max_val)


