import sys
sys.stdin=open('baekjoon/input.txt','r')

n=int(sys.stdin.readline())
a=[]
for i in range(n):
    info=list(map(str,sys.stdin.readline().split()))
    info[0]=int(info[0])
    info.append(i)
    a.append(info)
#나이순 오름차순, 나이가 같으면 순서별 오름차순
a.sort(key=lambda x:(x[0],x[2]))
for age,name,idx in a:
    print(age,name)

