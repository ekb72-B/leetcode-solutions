class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numdict = {}

        for index,value in enumerate(nums):
            diff = target - value
            if diff in numdict:
                return [index, numdict[diff]]
            else:
                numdict[value] = index



        

        