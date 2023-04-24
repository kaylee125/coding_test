#https://leetcode.com/problems/two-sum/


class Solution:
    #1.브루트포스로 계산: 모든 조합을 더해서 일일이 확인해보는 무차별 대입 방식(시간복잡도:O(n^2))
    def twoSum_brute(self, nums, target) :
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
    # target-nums[i]한 값이 리스트 나머지 값에 존재하면 enumerate로 index return
    def twoSum_enumerate(self,nums,target):
        for i,n in enumerate(nums):
            complement=target-n
            if complement in nums[i+1:]:
                print(nums[i+1:])
                return [nums.index(n),nums[i+1:].index(complement)+(i+1)]
    #첫번째 수를 뺀 결과 키 조회 
    def twoSum3(self,nums,target):
        nums_map={}
        #키와 값을 뒤바꿔 딕셔너리로 저장
        for i, num in enumerate(nums):
            nums_map[num]=i
        
        for i,num in enumerate(nums):
            #num을 뺀 값이 nums_map에 존재하고 i가 nums_map의 키값과 동일하지 않아야함
            if target-num in nums_map and i!=nums_map[target-num]:
                return[i,nums_map[target-num]]
     #twosum3에서 for문을 하나로 합쳐서 처리       
    def twoSum4(self,nums,target):
        nums_map={}
        for i,num in enumerate(nums):
            if target-num in nums_map:
                return [nums_map[target-num],i]
            nums_map[num]=i
   


solution=Solution()
nums = [3,2,4]
target = 6

result=solution.twoSum3(nums,target)
print(result)