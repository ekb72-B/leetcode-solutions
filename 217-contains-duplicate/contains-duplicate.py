class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ndict = set()
        for i in nums:
            if i in ndict:
                return True
            else:
                ndict.add(i)
                