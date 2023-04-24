class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        init=Node('init')
        self.head=init
        self.tail=init

        self.현재노드=None
        self.데이터수=0
    
    def append(self,data):
        새로운노드=Node(data)
        self.tail.next=새로운노드
        self.tail=새로운노드
        self.데이터수+=1

a=LinkedList()
a.append(1)  
a.append(2)
a.append(2)
a.append(1) 
print(a.head.data) 
print(a.head.next.data)
print(a.head.next.next.data)
print(a.head.next.next.next.data) 