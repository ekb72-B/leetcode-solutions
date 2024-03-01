class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        ntrue = 0

        for num in arr:
            if num %2 != 0:
                ntrue += 1
                if ntrue == 3:
                    return True
            
            else:
                ntrue = 0
        
        return False