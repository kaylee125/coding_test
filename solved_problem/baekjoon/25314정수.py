
n=int(input())
# answer=''
# for _ in range(n//4):
#     answer+='long '
# answer+='int'

answer=''.join('long ' for _ in range(n//4))

print(answer+'int')