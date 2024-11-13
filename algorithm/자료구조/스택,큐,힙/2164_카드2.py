from collections import deque


N=int(input())
cards=deque([n for n in range(1,N+1)])
last_card=0
while len(cards)>1:
    cards.popleft()
    cards.append(cards.popleft())

print(cards[0])







