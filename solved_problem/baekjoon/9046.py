

N=int(input())

for _ in range(N):
    string=input()
    
    dic={x:0 for x in string}
    
    if ' ' in dic.keys():
        del dic[' ']
    
    for x in string:
        if x in dic.keys():
            dic[x]+=1
    
    max_cnt=max(dic.values())
    cnt=0
    res=''
    for k,v in dic.items():
        if v==max_cnt:
            cnt+=1
            res=k
        
    if cnt>=2:
            print('?')        
    else:
        print(res)