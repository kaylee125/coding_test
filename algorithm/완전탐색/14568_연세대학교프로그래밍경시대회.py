N=int(input())

cnt=0
for a in range(0,N+1):
    for b in range(0,N+1):
        for c in range(0,N+1):
            if a+b+c==N:
                if a!=0 and b!=0 and c!=0:
                    if c>=b+2:
                        if a%2==0:
                            cnt+=1

print(cnt)
