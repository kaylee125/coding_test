"""

L	커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨): if cur!=0 일 경우 cur-=1
D	커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨):if len(list) !=cur 일 경우 cur +=1
B	커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨):list(cur-1)값을 delete 단 cur!=0일 경우에만 실행
삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임
P $	$라는 문자를 커서 왼쪽에 추가함
"""
import sys
sys.stdin=open('input.txt','r')

s=[x for x in sys.stdin.readline().rstrip()]
print(s)
T=int(sys.stdin.readline().rstrip())

for _ in range(T):
    cmd=sys.stdin.readline().split()
    print(cmd)
    cur=len(s)
    
    if cmd[0]=='P':
        if cur==len(s):
            s.append(cmd[1])
        else:
            b_a=s[cur:]
            f__a=s[:cur]
            f__a.append(cmd[1])
            f__a.extend(b_a)
    elif cmd[0]=='L':
        if cur!=0:
            cur-=1
            
    elif cmd[0]=='D':
        if len(s) !=cur :
            cur +=1
            
    elif cmd[0]=='B':
        if cur!=0:
            b_a=s[cur:]
            f__a=s[:cur]
            f__a.pop()
            f__a.extend(b_a)
            
    
print(s)        
        
            
#P
# if cur == len(a):
#     a.append('x')
# else:
#     b_a=a[cur:]
#     f__a=a[:cur]
#     f__a.append('x')
#     f__a.extend(b_a)
#     print(f__a)
# print(f__a)