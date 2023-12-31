class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # using xor 
        
        res = 0
        for i in nums:
            res ^= i
            
        return res