class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #generate an array of len nums and return value that is not there
        v = {}

        for num in nums:
            v[num] = num

        for i in range(len(v)):
            if i not in v:
                return i

        return 0 if 0 not in v else len(nums)
