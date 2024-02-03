class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # if the next item decreases the sum, set window to begin after it
        # if prev item decreases sum, remove it from the window 

        maxcurr = maxglobal = nums[0]

        for i in range(1, len(nums)):
            maxcurr = max(maxcurr + nums[i], nums[i])

            if maxcurr > maxglobal:
                maxglobal = maxcurr

        return maxglobal
        