#https://data-marketing-bk.tistory.com/31
'''1. 주어진 배열을 더 이상 쪼갤 수 없을 때까지 둘로 분할한다.
2. 나뉜 두 개의 배열을 하나로 합치는데, 이 때, 크기가 작은 값이 앞에 오도록 한다.
3. 배열의 크기가 기존과 같아질 때까지 병합 과정을 반복한다.'''
import sys
sys.stdin=open('solved_problem/baekjoon/input.txt','r')
input = sys.stdin.readline

def mergeSort(L):
    if len(L) == 1:
        return L
    
    mid = (len(L) + 1)//2
    left = mergeSort(L[:mid])
    right = mergeSort(L[mid:])
    
    L2 = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            L2.append(left[i])
            ans.append(left[i])
            i += 1
        else:
            L2.append(right[j])
            ans.append(right[j])
            j += 1
    
    while i < len(left):
        L2.append(left[i])
        ans.append(left[i])
        i += 1
        
    while j < len(right):
        L2.append(right[j])
        ans.append(right[j])
        j += 1
        
    return L2

n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = []
mergeSort(a)

if len(ans) >= k:
    print(ans[k-1])
else:
    print(-1) 