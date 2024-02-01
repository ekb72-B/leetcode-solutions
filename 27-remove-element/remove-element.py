class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # track viable loc1 and curr val
        vloc= 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[vloc] = nums[i]
                vloc += 1
        return vloc
