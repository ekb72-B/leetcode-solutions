class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # using xor 
        ctr = 0
        val = 0
        
        for i in nums:
            val ^= i

        return val