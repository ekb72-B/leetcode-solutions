class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n not in seen:
            seen.add(n)
            n = self.squareNum(n)

            if n == 1:
                return True 
        return False

    def squareNum(self, n):
        res = 0

        while n:
            digit = n % 10
            digit = digit ** 2
            res += digit
            n = n // 10


        return res

        