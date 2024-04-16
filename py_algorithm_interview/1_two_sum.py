class Solution(object):
    def twoSum(self, nums, target):
        for i,n in enumerate(nums):
            sub_n=target-n
            if sub_n in nums[i+1:] :
                return [nums.index(n),nums[i+1:].index(sub_n)+(i+1)]
                

sol=Solution()
nums = [3,2,3]
target = 6
res=sol.twoSum(nums,target)
print(res)