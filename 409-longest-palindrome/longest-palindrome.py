class Solution:
    def longestPalindrome(self, s: str) -> int:
        sset = set()
        totlen = 0

        for char in s:
            if char not in sset:
                sset.add(char)
            else:
                sset.remove(char)
                totlen += 2

        if len(sset) > 0 :
            totlen += 1
        
        return totlen


