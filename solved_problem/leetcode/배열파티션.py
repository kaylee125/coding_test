#https://leetcode.com/problems/array-partition/
#n개의 pair를 이용한 min(a,b)합으로 만들 수 있는 최대값
class Solution:
    #오름차순 풀이
    def arrayPairSum1(self, nums):
        nums.sort()
        sum=0
        pair=[]

        for n in nums:
            pair.append(n)

            if len(pair)==2:
                sum+=min(pair)
                pair=[]
        return sum
    #정렬한 리스트의 짝수번째 값이 항상 작은 값이라는 사실을 적용
    def arrayPairSum2(self, nums):
            nums.sort()
            sum=0
            for i,n in enumerate(nums):
                if i%2==0:
                    sum+=n
            return sum
    #파이써닉한 방법
    def arrayPairSum3(self,nums):
         return sum(sorted(nums)[::2])
    
solution=Solution()
nums=[1,4,3,2]
print(solution.arrayPairSum3(nums))            
        
