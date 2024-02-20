class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        stack = sorted(nums)[::-1]
    
        return stack[k - len(nums)-1]
