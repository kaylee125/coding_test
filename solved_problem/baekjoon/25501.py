def recursion(s, l, r,cnt):
    if l >= r: 
        return 1,cnt
    elif s[l] != s[r]: 
        return 0,cnt
    else: 
        cnt+=1
        return recursion(s, l+1, r-1,cnt)

def isPalindrome(s):
    cnt=0
    return recursion(s, 0, len(s)-1,cnt+1)

if __name__=='__main__':
    n=int(input())
    for _ in range(n):
        word=input()
        res=isPalindrome(word)
        for x in res:
            print(x,end=' ')