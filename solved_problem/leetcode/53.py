class Solution:
    # 문제: 주어진 Array에서 최대 Maximum Subarray를 계산하여라
    def maxSubArray(self,nums):
        #1.리스트의 길이가 0일때
        if len(nums)==0:
            return 0
        #2.리스트의 길이가 1일때
        if len(nums)==1:
            return nums[0]
        #3. 리스트의 길이가 2 이상일때
            # 현재 원소가 리스트의 마지막 원소라고 가정했을때 가장 최적의 값을 구해야함

        dp_arr=[0]*len(nums) #최적의 값을 저장하는 dp배열
        dp_arr[0]=nums[0]
        for i in range(1,len(nums)):
            prev_max=dp_arr[i-1]
            current=nums[i]

            connected_sum=prev_max+current
            # f(n)=max{In(n) , In(n)+f(n-1)}
            max_subarray=max(connected_sum,current)
            dp_arr[i]=max_subarray

        max_sum=max(dp_arr)
        return max_sum
    
nums=[1,2,3,4,5]    
print(Solution().maxSubArray(nums))
        