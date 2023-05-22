
def P(n):
    arr=[0]*(101)
    arr[1]=1
    arr[2]=1
    arr[3]=1
    for i in range(4,n+1):
        arr[i]=arr[i-2]+arr[i-3]
    return arr[n]

if __name__=='__main__':
    T=int(input())
    res=[]
    for _ in range(T):
        res.append(P(int(input())))
    for x in res:
        print(x)