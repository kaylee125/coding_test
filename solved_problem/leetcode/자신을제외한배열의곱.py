#https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums):
        out=[]
        p=1
        #왼쪽곱셈
        for i in range(0,len(nums)):
            out.append(p)
            p=nums[i]*p
        p=1
        #왼쪽곱셈결과에 오른쪽 값을 차례대로 곱셈
        for i in range(len(nums)-1,-1,-1):
            #왼쪽 결과값에 오른쪽 값을 차례로 곱셈
            out[i]=out[i]*p
            #오른쪽곱셈
            p=p*nums[i]

        return out
solution=Solution()
nums = [1,2,3,4]
print(solution.productExceptSelf(nums))