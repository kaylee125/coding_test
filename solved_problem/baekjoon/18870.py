import sys
sys.stdin=open('baekjoon/input.txt','r')
n=int(input())
arr=list(map(int,input().split()))
arr_set=sorted(set(arr)) #중복제거를 위해 리스트를 set로 만든 후 정렬
arr_dict={arr_set[i]:i for i in range(len(arr_set))}#딕셔너리로 저장 -> '숫자:arr_set에서의 해당 인덱스'

for i in arr:
    print(arr_dict[i],end=' ')
