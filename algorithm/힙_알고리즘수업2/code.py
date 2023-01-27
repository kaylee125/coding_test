#힙 정렬로 배열 A를 오름차순 정렬할 경우 배열 A의 원소가 K 번 교환된 직후의 배열 A를 출력해 보자
import sys
import heapq as hq

base='/Users/leesh970930/Desktop/git_codingtest/algorithm/힙_알고리즘수업1/'
sys.stdin=open(base+"in1.txt",'r')

n,k=map(int,input().split())
a=list(map(int,input().split()))
print(n,k,a)

