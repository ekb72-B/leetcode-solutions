class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        through indexing, multiply all items on the left and right and give an output in array of the result 
        '''
        res = []
        allmult = 1

        if 0 in nums:
            for i in range(len(nums)):
                right = self.multiply(nums[:i])
                left = self.multiply(nums[i+1:])
                res.append(right * left)

        else:
            for i in nums:
                allmult *= i

            for i in nums:   
                res.append(allmult//i)
        
        return res

    def multiply(self,nums):
        ans = 1
       
        for i in nums:
            ans *= i

        return ans