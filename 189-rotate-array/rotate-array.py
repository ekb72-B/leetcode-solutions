class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nk = k

        if len(nums) == 0:
            return []

        if k == 0:
            return nums
  
        if nk > 0:
            mk = k % len(nums)
        
        nums[:] = nums[-mk:] + nums[:-mk] 
        
        
    