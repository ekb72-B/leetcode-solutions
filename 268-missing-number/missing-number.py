class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #generate an array of len nums and return value that is not there
        v = [-1] * (len(nums) + 1)

        for num in nums:
            v[num] = num

        for i in range(len(v)):
            if v[i] == -1:
                return i

        return 0 
