'''
N개의 숫자로 이루어진 숫자열이 주어지면 해당 숫자열중에서 
s번째부터 e번째 까지의 수를 오름 차순 정렬했을 때 k번째로 나타나는 숫자를 출력하는 프로그램을 작성하세요.
'''
import sys
sys.stdin=open('/Users/leesh970930/Desktop/coding_algorithm/solved_problem/inflean/input.txt','r')

test=int(input())
info=[]
for t in range(test):
   n,s,e,k=map(int,input().split())
   a=list(map(int,input().split()))
   a=a[s-1:e]
   a.sort()
   print('#%d %d' %(t+1, a[k-1]))



