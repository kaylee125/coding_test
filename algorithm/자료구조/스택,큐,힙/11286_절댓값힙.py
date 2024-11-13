import heapq
import sys
input=sys.stdin.readline
N=int(input())
num_lst=[]

for _ in range(N):
    num=int(input())

    if num:
        heapq.heappush(num_lst,(abs(num),num))

    else:
        if num_lst:
            print(heapq.heappop(num_lst)[1])
        else:
            print(0)

        