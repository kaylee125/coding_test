class ListNode(object):
    def __init__(self,val=0,next=None,prev=None):
        self.val=val
        self.next=next
        self.prev=prev

class BrowserHistory(object):
    def __init__(self,hompage):
        self.head=self.current=ListNode(val=hompage)
    
    def visit(self,url):
        self.current.next=ListNode(val=url,prev=self.current)
        self.current=self.current.next
    
    def back(self,steps):
        while steps>0 and self.current.prev !=None:
            step-=1
            self.current=self.current.prev
        return self.current.val
    
    def forward(self,steps):
        while steps>0 and self.current.next!=None:
            step-=1
            self.current=self.current.next
        return self.current.val
        