class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if not n != 0 and n % 3 == 0:
            return False
        
        if n == 1:
            return True

        else:
            while n > 2:
                n = n / 3

            return n == 1
        