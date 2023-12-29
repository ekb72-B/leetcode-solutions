class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # use a pointer to go to a num and compare sums before and after
        sumbefore = 0
        sumafter = sum(nums)
        for i in range(len(nums)):
            sumafter -= nums[i]
            if sumbefore == sumafter:
                return i
            sumbefore += nums[i]
        return -1