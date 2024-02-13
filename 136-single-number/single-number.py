class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # using xor 
        ctr = 0
        val = 0
        n = sorted(nums)

        for i in n:
            if ctr == 0:
                val = i
                ctr += 1
            
            elif i == val:
                ctr = 0

        return val