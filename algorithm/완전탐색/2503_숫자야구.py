N=int(input())
tc_list=[list(map(int,input().split())) for _ in range(N)]
result=0

for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if i==j or j==k or k==i:
                continue
            
            cnt=0    
            for tc in tc_list:
                num=str(tc[0])
                strike=tc[1]
                ball=tc[2]

                ball_cnt=0
                strike_cnt=0
                
                candidate=[i,j,k]
                tc_num=[int(num[0]),int(num[1]),int(num[2])]

                for x in range(3):
                    if candidate[x]==tc_num[x]:
                        strike_cnt+=1
                    elif candidate[x] in tc_num:
                        ball_cnt+=1
                
                if ball_cnt==ball and strike_cnt==strike:
                    cnt+=1

            if cnt==N:
                result+=1                

print(result)
            




