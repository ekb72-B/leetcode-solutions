class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        
        #note : do not forget to eliminate already seen mid, thus + or - 1 as observed.
        while start <= end :
            mid = (start + end)//2 
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1