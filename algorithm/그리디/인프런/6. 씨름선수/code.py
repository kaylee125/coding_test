import sys 

base='/Users/leesh970930/Desktop/pythonalgorithm_formac/섹션 4/'
sys.stdin=open(base+'6. 씨름선수/in1.txt', "r")

n=int(input())
supplier=[]

for x in range(n):
    t,w= map(int,input().split())
    supplier.append(((t,w)))
supplier.sort(reverse=True)

#키를 내림차순으로 정렬 후 몸무게로만 비교하면 됨

largest=0
cnt=0
for t,w in supplier:
    if largest<w:
        cnt+=1
        largest=w
print(cnt)



