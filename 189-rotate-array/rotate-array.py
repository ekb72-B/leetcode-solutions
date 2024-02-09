class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nend = len(nums)-1
        nk = k

        if len(nums) == 0:
            return []

        if k == 0:
            return nums
  
        while nk > 0:
            nend -= 1
            nk -= 1
            mk = k % len(nums)
        
        nums[:] = nums[-mk:] + nums[:-mk] 
        
        
    