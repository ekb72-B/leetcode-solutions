class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currmax = globalmax = nums[0]

        for i in range(1, len(nums)):
            currmax = max(currmax + nums[i], nums[i])
            globalmax = max(globalmax, currmax)

        return globalmax