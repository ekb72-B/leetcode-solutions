class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numdict = set()
        for i in nums:
            if i in numdict:
                return True
            else:
                numdict.add(i)
                