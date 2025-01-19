import sys
sys.stdin=open('5. 동전분배하기/in4.txt','r')

def DFS(L):
    global res
    if L==n:
        cha=max(a)-min(a)
        if cha<res:
            #세개의 값이 서로 다른지 check
            tmp=set()
            for i in a:
                tmp.add(i)
            if len(tmp)==3:
                res=cha
    else:
        for i in range(3):
            a[i]+=coin[L]
            DFS(L+1)#다음 동전
            #더했던걸 다시 빼는 코드
            a[i]-=coin[L]
if __name__=="__main__":
    n=int(input())
    coin=[]
    for _ in range(n):
        coin.append(int(input()))
    a=[0,0,0]
    res=2222222
    DFS(0)
    print(res)