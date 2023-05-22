import sys
sys.stdin=open('baekjoon/input.txt','r')
n=int(input())
sanggeun=list(map(int,sys.stdin.readline().split()))
m=int(input())
cards=list(map(int,sys.stdin.readline().split()))

sanggeun=set(sanggeun)

#해시맵에 제시된 카드가 포함되어있으면 갯수를 리턴하고 없으면 0을 리턴한다.
for card in cards:
    if card in sanggeun:
        print(1,end=' ')
    else:
        print(0,end=' ')

