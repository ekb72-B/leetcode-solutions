class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # check current node, if it is less than target go right, if it is more go left

        start = 0 
        end = len(nums)-1

        if len(nums) == 1 and nums[0] == target:
            return 0

        while start <= end:
            mid = (start + end) //2 
            if nums[mid] < target:
                start = mid +1
            elif nums[mid] > target:
                end = mid - 1
            else:
                return mid
        return -1