
n=int(input())
emp=[]
star=[0]*(n*2-1)
for i in range(1,2*n):
    emp.append(abs(n-i)) #공백

for i in range((2*n+1)//2):
    star[i]=2*i+1
    star[2*n-2-i]=2*i+1

for k in range(len(star)):
    print(' '*emp[k]+'*'*star[k])






