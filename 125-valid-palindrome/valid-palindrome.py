class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        f = s.strip()
        p = ""
        for i in f:
            if i.isalnum():
                p+= i

        start = 0
        end = len(p)-1

        while start < end:
            p1 = p[start].lower()
            p2 = p[end].lower()
            if p1 != p2:
                return False

            start += 1
            end -= 1

        return True
