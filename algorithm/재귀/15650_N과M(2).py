"""
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
고른 수열은 오름차순이어야 한다.

"""

def recur(number,candi):
    if number==m:
        print(ans)
        result.append(ans)
        print ('result',result)
        return
    
    for i in range(1,n+1):

        recur(number+1,result)
        ans.pop()
    print(result)
    return result


n,m=map(int,input().split())
ans=[]
result=[]
recur(0,[])