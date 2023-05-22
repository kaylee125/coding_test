a,b,c=(map(int,input().split()))
result=0

if a==b and b!=c or a==c and a!=b:
    result=1000+100*a
elif b==c and a!=b:
    result=1000+100*b
elif a==b and b==c:
    result=10000+1000*a
else:
    result=max(a,b,c)*100

print(result)
