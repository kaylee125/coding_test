import sys
sys.stdin=open('baekjoon/input.txt','r')
n=int(input())
arr=[sys.stdin.readline().split() for _ in range(n)]
arr.sort(key=lambda x:x[1])
# print(arr)
dic_name={name:info for name,info in arr}  
print(dic_name)
# for name in dic_name:
#     if dic_name[name]=='enter':
#         print (name)
