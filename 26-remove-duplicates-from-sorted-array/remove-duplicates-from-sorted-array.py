class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        valdict = {}

        for i in nums:
            if i not in valdict:
                valdict[i] = 1
                nums[idx] = i
                idx += 1
            
        return idx 

            