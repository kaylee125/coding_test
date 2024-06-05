
"""

1.스택
    1)후입선출 방식의 자료구조- 가장 마지막에 쌓은 데이터를 가장 먼저 꺼냄
    
    2) 스택 구현시 필요한 매서드
        push(x): 리스트에 append
        pop(): 자료를 꺼내는 작업, 연결 리스트의 popleft와 같다.
        peek(): 마지막에 넣은 자료를 확인하는 작업으로 pop과 비슷하지만, 값을 제거하지 않음
        is_empty(): 빈 스택인지 확인하는 작업
        
    3)사용되는 문제 예시
        - 웹 브라우저 방문기록(뒤로가기)
        - 실행 취소(undo)
        - 역순 문자열 만들기
        - 수식의 괄호 검사(연산자 우선순위 표현을 위한 괄호검사)
        - 후위 표기법 계산

    
"""
# 파이썬으로 스택 구현
class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def size(self):
        return len(self.items)

    def top(self):
        if self.empty():
            return "stack is empty."
        return self.items[-1]

    def empty(self):
        return not self.items

    def __str__(self):
        return f"{self.items}"
    
    
def action_stack_class():
    stack = Stack()
    print(f"Make a stack : {stack}") #빈리스트 생성
    print(f"Is stack empty? {stack.empty()}")
    print()

    stack.push(2)
    print(f"Push 2 : {stack}")
    stack.push(3)
    print(f"Push 3 : {stack}")
    stack.push(9)
    print(f"Push 9 : {stack}")
    print(f"Is stack empty? {stack.empty()}")
    print()

    stack.pop()
    print(f"pop : {stack}")
    stack.pop()
    print(f"pop : {stack}")
    stack.pop()
    print(f"pop : {stack}")
    print(f"Is stack empty? {stack.empty()}")
    print()

    stack.push(1)
    print(f"Push 1 : {stack}")
    print(f"size of stack : {stack.size()}")
    stack.push(7)
    print(f"Push 7 : {stack}")
    print(f"Is stack empty? {stack.empty()}")
    print(f"size of stack : {stack.size()}")

    print()
    print(stack)
    print(f"top of stack : {stack.top()}")


"""
2.큐 
    1) 큐는 들어간 순서대로 출력됨(선입선출)
        큐는 한쪽 끝에서는 삽입 연산만 이루어지며 다른 한쪽 끝에서는 삭제 연산만 이루어지는 유한 순서 리스트
    
    2) 메소드
        큐 선언: queue=deque() ->collections에 deque import필요
        큐에 값 추가: queue.append(x)->x값 추가
        큐 값 반환/삭제: queue.popleft() ->맨 왼쪽 값  반환 및 삭제
    
    3) 큐의 포인터
        - front: 큐의 첫 번째 원소를 가리키는 포인터
        - rear: 큐의 마지막 원소를 가리키는 포인터
        - push(): 큐에 값을 넣는 연산 (Enqueue)
                rear 위치에 자료를 추가하고 rear를 1 증가시킴
        - pop(): 큐에서 자료를 빼는 연산 (Dequeue)
                front 위치에 자료를 제거하고 front를 1 증가시킴
        - front(): 큐의 가장 앞에 있는 자료를 반환하는 연산
        - back(): 큐의 가장 뒤에 있는 자료를 반환하는 연산
        - empty(): 비어있는지의 여부를 반환하는 연산

        * rear가 가리키는 인덱스가 배열의 크기를 초과하게 되면 문제가 생기는데, 이를 해결하기 위한 것이 '원형 큐'와 '링크드 큐'이다.

        
    3) 사용되는 문제 예시
        - 선입선출이 필요한 대기열 (티켓 카운터 or 게임같은 플랫폼)
        - BFS(Breadth-First Search, 너비 우선 탐색) 구현
        - 처리해야 할 노드의 리스트를 저장하는 용도
        - 우선순위가 같은 작업 예약 (인쇄 대기열)
        - 콜센터 고객 대기 시간
        - 프린터의 출력처리
        - 프로세스 관리(OS 관련 내용)
        - 덱(dequeue)
        
    4)큐의 종류 
        원형 큐
        - 원형 큐의 경우, front나 rear가 큐의 끝에 도달하면 이를 큐의 맨 앞으로 보내 문제를 해결한다.
 
        링크드 큐
        - 연결리스트로 구현한 큐를 의미한다.
        - 삽입과 삭제가 제한되지 않으며 크기의 제한이 없다    
"""
from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    '''
    노드를 삽입할 때
        빈 큐이면 front와 rear가 모두 첫 노드를 가리켜야 한다.
        빈 큐가 아니면 rear의 next가 추가 노드를 가리키게 한 후에, rear를 추가 노드로 옮긴다.
        
    노드를 꺼낼 때
        빈 큐가 되면 front와 rear는 모두 None을 가리켜야 한다.
        큐에 노드가 남아있으면 front를 front의 next로 옮긴다.'''
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        #append
        if self.front is None:
            self.front = self.rear = Node(data) #빈 큐이면 front와 rear가 모두 첫 노드를 가리켜야 한다
        else:
            node = Node(data)
            self.rear.next = node #rear의 next가 추가 노드를 가리키게 한 후에
            self.rear = node #rear를 추가 노드로 옮긴다.

    def dequeue(self):
        if self.front is None:
            return None 
        node = self.front
        if self.front == self.rear:
            self.front = self.rear = None #빈 큐가 되면 front와 rear는 모두 None을 가리켜야 한다.
        else:
            self.front = self.front.next 
        return node.data

    def is_empty(self):
        return self.front is None


def action_queue_class():
    q = Queue()

    for i in range(3):
        q.enqueue(chr(ord("A") + i))
        print(f"Enqueue data = {q.rear.data}")
    print()

    while not q.is_empty():
        print(f"Dequeue data = {q.dequeue()}")
        
        
        
if __name__ == "__main__":
     
    print('stack')   
    action_stack_class()
    
    
    print('queue')
    action_queue_class()