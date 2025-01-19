
"""
호출 순서
시작: recur(0, 0, 0, 0, 0, 0, [])

재료 1 사용 X: recur(1, 0, 0, 0, 0, 0, [])
    재료 2 사용 X: recur(2, 0, 0, 0, 0, 0, [])
        재료 3 사용 X: recur(3, 0, 0, 0, 0, 0, []) → 탐색 종료
        재료 3 사용 O: recur(3, 50, 10, 20, 3, 60, [3]) → 기준 미충족 → 탐색 종료
    재료 2 사용 O: recur(2, 40, 40, 40, 2, 50, [2])
        재료 3 사용 X: recur(3, 40, 40, 40, 2, 50, [2]) → 기준 미충족 → 탐색 종료
        재료 3 사용 O: recur(3, 90, 50, 60, 5, 110, [2, 3]) → 기준 미충족 → 탐색 종료
재료 1 사용 O: recur(1, 30, 20, 50, 5, 40, [1])
    재료 2 사용 X: recur(2, 30, 20, 50, 5, 40, [1])
        재료 3 사용 X: recur(3, 30, 20, 50, 5, 40, [1]) → 기준 미충족 → 탐색 종료
        재료 3 사용 O: recur(3, 80, 30, 70, 8, 100, [1, 3]) → 기준 미충족 → 탐색 종료
    재료 2 사용 O: recur(2, 70, 60, 90, 7, 90, [1, 2])
        재료 3 사용 X: recur(3, 70, 60, 90, 7, 90, [1, 2]) → 기준 미충족 → 탐색 종료
        재료 3 사용 O: recur(3, 120, 70, 110, 10, 150, [1, 2, 3]) → 기준 충족 → 최저비용 갱신

"""
def recur(idx,p,f,s,v,c,idx_ingred):
    global min_cost,final_ingred
    
    #최소기준 만족했으면 최저비용 업데이트
    if p>=mp and f>=mf and s>=ms and v>=mv: #최저 영양 기준에 만족 한 경우 
        if c<min_cost: #최저비용보다 비용이 작은 경우 최저비용,재료조합 갱신
            min_cost=c
            final_ingred=[idx_ingred[:]]
        elif c==min_cost: #기존 최저비용과 비용이 동일한 경우 최저비용 유지, 재료조합 추가
            final_ingred.append(idx_ingred)
        return 

    #모든 재료를 탐색한 경우 함수 종료
    if idx==N:
        return 

    #식재료 사용 x -> 다음 재료 탐색
    recur(idx+1,p,f,s,v,c,idx_ingred)

    #식재료 사용 o -> 다음 재료 탐색,영양소,비용 값 증가,현재 재료 선택
    recur(idx+1,p+ingreds[idx][0],f+ingreds[idx][1],s+ingreds[idx][2],v+ingreds[idx][3],c+ingreds[idx][4],idx_ingred+[idx+1])


N=int(input())
mp,mf,ms,mv=map(int,input().split())
ingreds=[list(map(int,input().split())) for _ in range(N)]
p=f=s=v=c=0
min_cost=9999999
final_ingred=[]
res=recur(0,p,f,s,v,c,[])

"""
출력 조건
첫 번째 줄에 최소 비용을 출력하고, 
두 번째 줄에 조건을 만족하는 최소 비용 식재료의 번호를 공백으로 구분해 오름차순으로 한 줄에 출력한다. 

같은 비용의 집합이 하나 이상이면 사전 순으로 가장 빠른 것을 출력한다.

조건을 만족하는 답이 없다면 -1을 출력하고, 둘째 줄에 아무것도 출력하지 않는다.

"""


if min_cost==9999999:
    print(-1)

else:
    print(min_cost)
    final_ingred.sort()
    print(*final_ingred[0])

