
word=input()
c=['c=','c-','dz=','d-','lj','nj','s=','z=']
cnt=0

for x in c:
    if x in word:
        word=word.replace(x,'a')
print(word)
print(len(word))


