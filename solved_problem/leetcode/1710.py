#https://leetcode.com/problems/maximum-units-on-a-truck/

class Solution:
    def maximumUnits(self, boxTypes,truckSize):
        boxTypes=sorted(boxTypes,key=lambda x:x[1],reverse=True)
        total_unit=0
        for box_count,unit in boxTypes:
            if box_count<=truckSize:
                total_unit+=box_count*unit
                truckSize-=box_count
            else:
                total_unit+=truckSize*unit
                truckSize-=truckSize
            if truckSize==0:
                return total_unit
            
        return total_unit

boxTypes =  [[3,1],[2,2],[1,4],[2,3]]
truckSize = 4
print(Solution().maximumUnits(boxTypes,truckSize))