##강의듣기

import sys
sys.stdin=open('/Users/leesh970930/Desktop/coding_algorithm/solved_problem/inflean/input.txt','r')

n=int(input())
student=list(map(int,input().split()))
min_val=100
avg=round(sum(student)/n,0)
sub=[]
for i in range(n):
    difference=abs(student[i]-avg)
    sub.append(difference)

a=[]
for x in range(n):
    if min(sub)==sub[x]:
        a.append(x)

max_value=0
for k in a:
    if max_value==student[k]:
        break
    if max_value<=student[k]:
        max_value=student[k]
print(max_value,k)     
