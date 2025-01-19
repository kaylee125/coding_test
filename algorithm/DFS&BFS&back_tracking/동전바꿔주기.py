import sys
sys.stdin=open('4. 동전바꿔주기/in2.txt',"r")

def DFS(L,sum):
    global cnt
    if sum>T:
        return
    if L==n:
        if sum==T:
            cnt+=1
    else:
        for i in range(coin_n[L+1]):
            DFS(L+1,sum+(coin_v[L]*i))

if __name__=="__main__":
    T=int(input())
    n=int(input())
    coin_v=[]#동전 가격
    coin_n=[]#동전 개수
    for _ in range(n):
        a,b=map(int,input().split())
        coin_v.append(a)
        coin_n.append(b)
    cnt=0
    DFS(0,0)
    print(cnt)

