'''
주어진 각 문제를 풀지 말지 결정하는 문제
부분집합의 경우의 수 생각하기

'''
import sys 

base='/Users/leesh970930/Desktop/pythonalgorithm_formac/섹션 7/'
sys.stdin=open(base+'1. 최대점수 구하기/in1.txt', "r")

def DFS(L,sum,time):
    global res
    if time>m: #cut-edge
        return
    #종착지점
    if L==n:
        if res<sum:
            res=sum
    #가지가 뻗어나가는 부분
    else:
        #L번째 문제를 풀 경우
        DFS(L+1,sum+pv[L],time+pt[L])
        #L번째 문제 안 풀 경우 
        DFS(L+1,sum,time)

if __name__=='__main__':
    n,m=map(int,input().split())
    pv=[]#점수
    pt=[]#걸리는 시간
    for _ in range(n):
        a,b=list(map(int,input().split()))
        pv.append(a)
        pt.append(b)
    res=0 #가장 작은 값으로 초기화하고 갱신시킨다.
    DFS(0,0,0)#level,총점,시간
    print(res)


