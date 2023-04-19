#이중for문으로 푸는 방법
#i부터 j까지 순회하면서 cnt 누적
def solution(i, j, k):
    cnt=0
    for n in range(i,j+1):
        n=str(n)
        for j in range(len(n)):
            j=int(j)
            
            if int(n[j])==k:
                cnt+=1

    
    return cnt

# def solution(i, j, k):
#     answer = 0
#     for num in range(i, j + 1):
#         if str(k) in str(num):
#             print('k:',str(k),'num:',str(num))
#             answer += str(num).count(str(k))
#     return answer

print(solution(1,13,1))