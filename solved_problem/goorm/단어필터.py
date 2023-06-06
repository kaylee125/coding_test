import sys
input=sys.stdin.readline
s_len,e_len = map(int,input().split())
s=input().rstrip()
e=input().rstrip()

while s in e:
	e=e.replace(s,'')
	print(e)
	
if e:
	print(e)
else:
	print('EMPTY')