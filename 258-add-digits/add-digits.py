class Solution:
    def addDigits(self, num: int) -> int:

        return self.digSplit(num)
    
    def digSplit(self,num):
        res = 0
        res += num % 10
        res += num//10

        if len(str(res)) > 1:
            return self.digSplit(res)

        return res