#https://leetcode.com/problems/3sum/
#브루트포스로 풀면 timeout
#투포인터로 푼다

class Solution:
    def threeSum(self, nums):
        results=[] 
        nums.sort()

        for i in range(len(nums)-2):
            #중복된 값 건너뛰기
            if i>0 and nums[i]==nums[i-1]:
                continue
            #간격을 좁혀나가면서 sum계산
            left,right=i+1,len(nums)-1
            while left<right:
                #3개의 수의 합을 구한다
                sum=nums[i]+nums[left]+nums[right]
                if sum<0:
                    left+=1
                elif sum>0:
                    right-=1
                else: 
                    #sum==0인 경우
                    results.append([nums[i],nums[left],nums[right]])
                    
                    #중복되는 값 건너 뛰고 두 포인터를 각각 오,왼쪽으로 옮긴후 다음 for문 진행
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
        return(results)
    

solution=Solution()
nums=[-1,0,1,2,-1,-4]
print(solution.threeSum(nums))