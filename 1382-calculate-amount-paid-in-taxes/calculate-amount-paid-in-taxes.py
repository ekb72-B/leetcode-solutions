class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        '''

        '''

        taxable = income
        already = 0
        res = 0

        for i in brackets:
            # how many of the taxable dollars to tax now?
            # take the number at index 0 minus already taxed 
            curr = min(income,i[0]) - already 
            already += curr
            taxable -= already
            res += (curr * (i[1]/100))
        
        return res