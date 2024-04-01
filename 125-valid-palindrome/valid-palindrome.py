class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        f = s.strip()
        p = ""
        for i in f:
            if i.isalnum():
                p+= i.lower()

        start = 0
        end = len(p)-1

        while start < end:
            p1 = p[start]
            p2 = p[end]
            if p1 != p2:
                return False

            start += 1
            end -= 1

        return True
