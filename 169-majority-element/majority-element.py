class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # simple boyer-moore voting algorithm
        mval , count = None, 0

        for num in nums:
            if count == 0:
                mval = num
                count += 1
            else:
                if num == mval:
                    count += 1
                else:
                    count -= 1
        
        return mval 

        