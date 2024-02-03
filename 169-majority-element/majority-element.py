class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # binary search?
        start = 0
        end = len(nums)-1
        mid = start + end //2
        nums = sorted(nums)

        
        return nums[mid]

        