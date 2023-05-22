import sys

a,b=map(str,input().split())
rev_a=a[::-1]
rev_b=b[::-1]
print(max(int(rev_a),int(rev_b)))