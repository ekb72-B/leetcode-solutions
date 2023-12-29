class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # use a pointer to go to a num and compare sums before and after
        sumbefore = sumafter = start = 0
        res = -1
        for i in range(len(nums)):
            sumbefore = sum(nums[:i])
            sumafter = sum(nums[i+1:])
            if sumbefore == sumafter :
                res = i
                return res
        return res