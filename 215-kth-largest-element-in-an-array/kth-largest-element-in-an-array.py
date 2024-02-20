class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        stack = sorted(nums)[::-1]
     
        for i in range(k-1):
            stack.pop(0)

        return stack[0]
