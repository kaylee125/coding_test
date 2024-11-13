from bisect import bisect_left,bisect_right
#bisect_left:x보다 크거나 같은 값들 중 가장 첫 번째 위치의 인덱스를 반환합니다1.
# 리스트에 x와 동일한 값이 있는 경우, 그 값의 인덱스를 반환합니다1.

#bisect_right:x보다 큰 값들 중 가장 첫 번째 위치의 인덱스를 반환합니다1.
# 리스트에 x와 동일한 값이 있는 경우, 그 값의 바로 다음 인덱스를 반환합니다1.

"""
5
4 1 5 2 3
5
1 3 7 9 5

7
1 2 3 3 3 4 5
5
1 3 5 7 3
"""
N=int(input())
a=sorted(list(map(int,input().split())))
M=int(input())
m=list(map(int,input().split()))

print('a',a)

for num in m:
    l=(bisect_left(a,num))
    h=(bisect_right(a,num))
    print(f'l:{l} h:{h} num:{num}')
    if h-l>0: #h-l ->a에 몇개의 num이 있는지
        print(1)
    else: 
        print(0)