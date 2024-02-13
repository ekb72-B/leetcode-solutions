class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numdict = {}

        for num in nums:
            if num in numdict: 
                numdict[num] += 1

            else:
                numdict[num] = 1

        
        for key,value in numdict.items():
            if value == 1:
                return key

            
                

