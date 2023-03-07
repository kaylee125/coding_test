'''
1.아이디어
-양팔저울의 모양을 잘 생각해보기
-각각의 추가 오른쪽,왼쪽, 사용하지 않을 3가지 경우에 대한 부분집합 경우의 수를 구하는 문제
    오른쪽에 위치할 경우 (+추의무게) 왼쪽에 위치할 경우(-추의무게), 위치하지 않을 경우(변동없음)
-측정 불가능한 물의 무게는 몇개인지 구하는 문제
    -1g~sg까지의 총 s개의 경우의 수 존재
    -중복을 제거한 측정 가능한 물의 무게의 갯수 구한 뒤 s에서 빼줌(set으로 구현)
2.자료구조
추의갯수:int k
각 추의 무게 : list a
측정 가능한 물의 무게 집합: set res

'''
import sys 
sys.stdin=open('3. 양팔저울/in2.txt', "r")

def DFS(L,sum):
    global res
    if L==k:
        if 0<sum<=s:
            res.add(sum)
            #양의 정수 값을 갖는 측정 가능한 물의 무게를 res에 추가
    else:
        #L무게의 추가 왼쪽에 위치
        DFS(L+1,sum+a[L])
        #추가 오른쪽에 위치
        DFS(L+1,sum-a[L])
        #위치하지 않을떄
        DFS(L+1,sum)
        
if __name__=='__main__':
    k=int(input())
    a=list(map(int,input().split()))
    s=sum(a)
    res=set()
    DFS(0,0) #레벨,물의 무게
    print(s-len(res))
