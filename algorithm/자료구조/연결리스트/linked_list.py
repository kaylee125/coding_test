"""
- linked list란 물리적으론 연속적이지 않지만 논리적으론 연속적으로 순서가 이어져있는 자료구조를 말함
- array list과 다르게 원소 값을 서로 다른 메모리에 저장할 수 있기 때문에 메모리를 효율적으로 사용할 수 있는 장점이 있지만, 
    각 노드가 next값을 가지고 있어야하기 때문에 노드별 차지하는 메모리 용량은 array list에 비해 더 큼
- linked list는 head값을 초기값으로 None값을 가지고 있다가 노드가 추가되는 순간 첫번째 노드를 가리킴.

"""

class Node():
    def __init__(self,value=0,next=None):
        self.value=value
        self.next=next


class Linkedlist(object):
    def __init__(self):
        self.head=None 
    def append(self,value):
        new_node=Node(value)

        if self.head is None:
            self.head=new_node
        else:
            current=self.head
            while(current.next): 
                current=current.next
            current.next=new_node
    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=' -> ')
            current = current.next
        print('None')  # End of list



ll=Linkedlist()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)


#연결 리스트의 값을 출력하기
ll.print_list()