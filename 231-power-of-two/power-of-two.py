import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # check if it's even. if it is, then check if it's a power

        if n <= 0:
            return False

        logn = math.log2(n)
        return logn.is_integer()