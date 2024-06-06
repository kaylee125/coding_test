"""
문제설명: 주어지는 단어들 위로 곡선을 그려 짝지었을때 곡선이 서로 만나지 않으면서 
        짝지어질 경우 좋은단어로 판별하자. 좋은단어의 갯수를 구하는 문제
핵심내용: 단순 스택 구현 문제
"""
import sys
sys.stdin=open('input.txt','r')

N=int(sys.stdin.readline())
cnt=0
for _ in range(N):
    word=sys.stdin.readline().rstrip()
    stack=[]
    
    for w in word:
        if stack:
            if stack[-1]==w:
                stack.pop()
            else:
                stack.append(w)
        else:
            stack.append(w)

    if not stack:
        cnt+=1

print(cnt)