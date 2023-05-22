import sys
sys.stdin=open('baekjoon/input.txt','r')

max_idx=0
max_val=0
for i in range(9):
    val=int(input())
    if max_val<val:
        max_val=val
        max_idx=i+1
print(max_val)
print(max_idx)