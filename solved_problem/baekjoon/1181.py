import sys
sys.stdin=open('input.txt','r')

n=int(input())
w_arr=[]
words=[]

for _ in range(n):
    words.append(sys.stdin.readline().rstrip())
words.sort()

for i in range(1,51): #단어의 길이   
    for word in words:
        if len (word)==i and word not in w_arr:#단어의 길이가 짧은것 부터 count/중복제거
            w_arr.append(word)

for x in w_arr:
    print(x)
