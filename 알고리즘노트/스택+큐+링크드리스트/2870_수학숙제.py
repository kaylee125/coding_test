import sys
sys.stdin=open('input.txt','r')

K=int(sys.stdin.readline().rstrip())

words=[]

for _ in range(K):
    word=sys.stdin.readline().rstrip()
    n=''
    for i,w in enumerate(word):
        if w.isdigit() :
            n+=w
            if i==len(word)-1:
                words.append(n)
        else:
            if n:
                words.append(n)
            n=''
res=[]

for word in words:
    if word :
        res.append(int(word))
           
for x in sorted(res):
    print(x)