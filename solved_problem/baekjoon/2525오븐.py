import sys

a,b=list(map(int,sys.stdin.readline().split()))
c=int(sys.stdin.readline())
b=b+c
while True:
    if b>=60:
        b=b-60
        a+=1
    else:
        break
if a>=24:
    a=a-24
print(a,b)
