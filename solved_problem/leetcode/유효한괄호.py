# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s) :
        stack=[]
        table={
            ')':'(',
            ']':'[',
            '}':'{'
        }

        for char in s:
            if char not in stack: #여는 괄호일 경우에만 스택에 append
                stack.append(char)
            # 반복문 도중에 스택에 더이상 값이 없거나 스택의 마지막값과 char에 대한 table value(여는 괄호)가 일치하지 않으면 return False
            elif not stack or table[char] !=stack.pop():
                return False
        #반복문이 종료했을 시점에 stack이 비어있다면 return True
        if len(stack)==0:
            return True
        
    
s = "()"
s2 = "()[]{}"
print(Solution().isValid(s))