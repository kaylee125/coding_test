def check_hint(idx,num):
    """
    아래 기본 전제 2가지 조건에 통과하지 못했다면 false반환
    - 세 자리 숫자는 서로 다른 수
    - 세 자리 숫자 각각은 0이 아님(1~9)

    만약 숫자가 힌트에 통과했다면 true반환
    - 스트라이크에 통과
        :동일한 위치에 동일한 숫자일 경우 1
    - 볼에 통과
        :다른 위치에 동일한 숫자일 경우 1

    통과하지 못했다면 False 반환 
    """
    strike=0
    ball=0

    tc_num=str(tc[idx][0])
    tc_strike=tc[idx][1]
    tc_ball=tc[idx][2]

    tc_n_list=[int(tc_num[0]),int(tc_num[1]),int(tc_num[2])]

    num=str(num)
    n_list=[int(num[0]),int(num[1]),int(num[2])]

    if n_list[0]==n_list[1] or n_list[1]==n_list[2] or n_list[0]==n_list[2]:
        return False
    
    if 0 in n_list:
        return False

    for i in range(3):
        if n_list[i]==tc_n_list[i]:
            strike+=1
        elif n_list[i] in tc_n_list :
            ball+=1

    if strike==tc_strike and ball==tc_ball:

        return True
    
    else:
        return False
    

def recur(hint_idx,num):
    global result

    if hint_idx==N:
        #모든 힌트에 통과한 경우 결과에 카운트
        result+=1
        recur(0,num+1)
        return  
    if num==1000:
        #999까지 유효한 숫자이므로 1000 이상 넘어가면 리턴
        return 

    #힌트에 통과했다면 동일한 숫자에 대해 다음 힌트 체크
    if check_hint(hint_idx,num):
        recur(hint_idx+1,num)

    #만약 힌트에 통과하지 않았다면
    #다음숫자로 넘어가서 처음 힌트부터 확인하기
    else:
        recur(0,num+1)


N=int(input())
tc=[list(map(int,input().split())) for _ in range(N)]
result=0


recur(0,111)
print(result)