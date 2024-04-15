# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # binary search between 1 and n
        start = 0
        end = n
        mid = (start + end)//2 
     
        # stop condition is when you find bad version
        
        '''
        [1, 2, ..., n]

        [g1, g2, g3, b4, b5]

        '''
        lowest = n

        if n <=1 :
            return n

        if isBadVersion(start):
            return start
        
        while mid > start and mid < end:
            if isBadVersion(mid):
                lowest = min(lowest,mid)
                end = mid
                mid = (start+end)//2
            if not isBadVersion(mid):
                start = mid
                mid = (start+end)//2

        return lowest

        





