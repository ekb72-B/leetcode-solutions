class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numdict = {}
        for i in range(len(nums)):
            if nums[i] not in numdict:
                numdict[nums[i]] = i
            else:
                return True
        return False