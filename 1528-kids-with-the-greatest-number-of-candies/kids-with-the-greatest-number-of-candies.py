class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        '''
        set a max variable that holds the biggest thing in list

    
        '''
        maxvar = max(candies)
        res = []

        for i in candies:
            if i + extraCandies >= maxvar:
                res.append(True)
            elif i + extraCandies < maxvar:
                res.append(False)
        return res
        