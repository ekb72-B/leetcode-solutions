class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)

        slow = 2
        fast = 2

        while fast < len(nums):
            if nums[fast] != nums[slow-2]:
                # number is not a repeat
                nums[slow] = nums[fast]
                slow += 1
                fast += 1

            else: 
                # it is a repeat, therefore go look for non repeat value
                fast += 1

        return slow