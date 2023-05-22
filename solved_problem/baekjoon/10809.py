S=input()
arr=[-1]*26

for idx,s in enumerate(S):
    trans_alpha=ord(s)-97
    if arr[trans_alpha] ==-1:
        arr[trans_alpha]=idx
for s in arr:
    print(s,end=' ')
