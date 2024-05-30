
"""
문제설명: 가장 빈번하게 나타나는 문자를 출력하거나 빈번하게 나타나는 문자가 여러 개일 경우 '?'를 출력
핵심내용: 알파벳 별 빈도수를 어떻게 count할것인지. 1157번과 매우 유사한 문제
시간복잡도: O(N)
"""
N=int(input())

for _ in range(N):
    string=input()
    
    dic={x:0 for x in string}
    
    # 공백 제외
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