#https://leetcode.com/problems/palindrome-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head:ListNode) -> bool:

        q=[]
        node=head

        while node is not None:
            q.append(node.val)
            node=node.next
            
        #펠린드롬 판별
        while len(q)>1:
            if q.pop(0) != q.pop():
                return False
        return True
    


solution=Solution()
head = [1,2,2,1]
print(solution.isPalindrome(head))

