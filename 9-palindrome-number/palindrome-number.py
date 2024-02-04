class Solution:
    def isPalindrome(self, x: int) -> bool:
        sx = str(x)
        st = 0
        end = len(sx)-1

        while st < end:
            if sx[st] != sx[end]:
                return False
            
            st += 1
            end -= 1 

        return True