def solution(s):
    
    len_s=len(s)
    cnt=0
    binary_cnt=0
    
    while s!='1':#문제조건:s가 "1"이 될 때까지 계속해서 s에 이진 변환을 가함
        new_s=[]
        for i  in range(len(s)):
            if s[i]=='0':
                cnt+=1 #제거한 '0'개수 Count
            else:
                new_s.append(s[i])
        s=''.join(new_s) #0제거한 문자열
                
        len_s=len(s)
        change_val=''
        #이진수 변환
        while len_s>=1:
            change_val+=str(len_s%2)
            len_s=len_s//2
            
        binary_cnt+=1#이진변환횟수 count

        #문자열을 바로 뒤집을 수 있는 방법으로 list로 변환 후 reverse함수로 뒤집은 다음 다시 join으로 묶는 방법을 선택함.
        change_val=list(str(change_val))
        change_val.reverse()
        s=''.join(change_val) #이진변환결과 '110' '10' '1'
        
    answer = [binary_cnt,cnt]
    return answer
# print(solution(	"110010101001"))
# print(solution(	"01110"))
print(solution("1111111"))
