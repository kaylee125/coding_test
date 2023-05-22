#주어진 수열 중 연속된 몇개의 수를 선택한 합 중 가장 큰 합, 숫자는 한개 이상 선택해야함.

import sys
input =sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))

if len(arr)==1:
    print (arr[0])
else:
    dp=[0]*len(arr)
    dp[0]=arr[0]
    #현재 원소가 리스트의 마지막 원소인것으로 가정했을때 max(dp의 i-1까지의 최적값+현재값,현재값)을 구하고 
    # max_sum값과 비교했을때 더 크면 max_sum값을 업데이트
    # dp[i-1]+현재값>현재값인 경우 i부터 새롭게 연속합을 해야함 
    for i in range(1,len(arr)):
        prev_max=dp[i-1]
        current_val=arr[i]

        choose=max(current_val,prev_max+current_val)
        dp[i]=choose

    max_subarray_sum=max(dp)
    print(max_subarray_sum)

