
## 이중for문 시간 초과
# a=input()
# a=a[::-1]
# res=''
# for i in range(0,len(a),3):
#     num=a[i:i+3]
#     print(num)
#     octal=0
#     for i in range(len(num)):
#         if num[i]=='1':
#             octal+=2**i
#     res+=''.join(str(octal))
# print(int(res[::-1]))

"""
**파이썬 format함수 사용**
2진수는 Binary format의 'b'
8진수는 Octal format의 'o'
16진수는 Hexadecimal format의 'x'"""

a=int(input(),2) #이진수 to 십진수
print(format(a,'o'))
