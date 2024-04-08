class Solution(object):
    def longestPalindrome(self, s):
        res=[]
        if len(s)==1:
            return s
        else:
            for i in range(0,len(s)):
                for j in range(i+1,len(s)+1):
                    word=s[i:j]
                    if word==word[::-1]:
                        res.append(word)
            if res: 
                return sorted(res,key=lambda x:len(x))[-1]    

    
solution=Solution()
s = "babad"
res=solution.longestPalindrome(s)
print(res)
