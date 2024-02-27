class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # based on the length, if u see a val in the range then whatev if not rhen return it

        lim = len(nums)
        
        res = float("-inf")
        for i in range(lim):
            if i not in nums:
                res = i
                break

        return res if res >= 0 else len(nums)
