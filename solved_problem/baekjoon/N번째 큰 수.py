import sys
import heapq as hq

sys.stdin=open('/Users/leesh970930/Desktop/coding_algorithm/solved_problem/baekjoon/input.txt','r')

n=int(input())
num=[[0]*n for _ in range(n)]
for _ in range(n):
    hq.heappush(num)
print(num)