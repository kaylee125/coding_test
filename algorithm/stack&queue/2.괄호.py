
# def solution(s):
#     stack=[]

#     for i in range(len(s)):
#         #만약 s[i]가 여는 괄호면 스택에 추가
#         if s[i]=='(':
#             stack.append(s[i])

#         #닫힌 괄호면 바로 앞에 문자 확인
#         else:
#             #앞에 문자가 여는괄호면:올바른 괄호->pop
#             if s[i-1]=='(':
#                 stack.pop()
#             elif s[i-1]==')':
#                 stack.append(s[i])
#             #앞에 문자가 닫는 괄호면:올바르지 않은 괄호->stack에 ')' append
#     print(stack)

stack=[]
s="()()"
for i in range(len(s)):
    #만약 s[i]가 여는 괄호면 스택에 추가
    if s[i]=='(':
        stack.append(s[i])

    #닫힌 괄호면 바로 앞에 문자 확인
    else:
        #앞에 문자가 여는괄호면:올바른 괄호->pop
        if s[i-1]=='(':
            stack.pop()
        elif s[i-1]==')':
            stack.append(s[i])
        #앞에 문자가 닫는 괄호면:올바르지 않은 괄호->stack에 ')' append
print(stack)