
"""
1-N번까지의 숫자 중  M개의 유효한 순열을 뽑아야함


"""

def recur(number):
    if number==m:
        print(*ans)
        return 
    
    for i in range(1,n+1): 
        if i in ans:
            continue
        ans.append(i)
        recur(number+1)
        ans.pop()#재귀 호출이 끝나고 돌아왔을 때, 마지막에 추가한 숫자를 제거하기 위해 ->다음 i의

n,m=map(int,input().split()) 
ans=[]
recur(0)

