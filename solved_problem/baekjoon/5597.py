import sys
sys.stdin=open('baekjoon/input.txt','r')

# students=[int(input() for _ in range(28))]
students=[]
ans=[]
for _ in range(28):
    a=int(input())
    students.append(a)
for i in range(1,31):
    if i not in students:
        ans.append(i)
ans.sort()
print(ans[0])
print(ans[1])