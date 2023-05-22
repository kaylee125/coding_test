import sys

sys.stdin=open('baekjoon/input.txt','r')
cnt=0
s=input()
for x in s:
    if x.isalpha():
        cnt+=1
print(cnt)