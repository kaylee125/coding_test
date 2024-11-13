"""
5
6 3 2 10 -10
8
10 9 -5 2 3 4 5 -10  """

N=int(input())
cards= sorted(list(map(int,input().split()))) #정렬
M=int(input())
nums=list(map(int,input().split()))

def isin(num):
    lo=0 #리스트의 최소 인덱스
    hi=N-1 #리스트의 최대 인덱스
    mid=lo+hi//2
    while lo<=hi:
        # print(f'lo:{lo} hi:{hi} mid:{mid}' )
        if cards[mid]==num:
            return True
        elif cards[mid]>num:
            hi=mid-1
        elif cards[mid]<num:
            lo=mid+1
        mid=(lo+hi)//2
    return False
    

for num in nums:
    if isin(num):
        print(1,end=' ')
    else:
        print(0,end=' ')
