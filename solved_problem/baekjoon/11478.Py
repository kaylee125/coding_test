import sys
sys.stdin=open('baekjoon/input.txt','r')
n=input()
cnt=0
a=[]
for i in range(len(n)):#글자갯수 1,2,3,4,5
    for j in range(i,len(n)):
        a.append(n[i:j+1])

print(len(set(a)))