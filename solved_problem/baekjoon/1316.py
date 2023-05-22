import sys
sys.stdin=open('baekjoon/input.txt','r')
# n=int(input())
# cnt=0
# for _ in range(n):
#     word=input()
#     ans=True
#     cont=''
#     for x in word:
        
#         if len(cont)==0 or x not in cont:
#             ans=True
#             cont+=x
#         #연속문자인 경우 
#         elif x in cont and cont[-1]==x:
#             ans=True
#             cont+=x
#         #연속문자가 아닌 경우
#         else:
#             ans=False
#             break
        
#     if ans==True:
#         cnt+=1
# print(cnt)

result = 0
re = int(input())
for i in range(re) : 
    word = input() 
    print(sorted(word, key=word.find)) #알파벳 순서대로 정렬 
    if list(word) == sorted(word, key=word.find): 
        result += 1

print(result)


    
        
        