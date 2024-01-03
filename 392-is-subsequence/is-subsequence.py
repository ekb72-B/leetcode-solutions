class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # use 2 pointers and only move forward if the pointers are touchign same char
        i = 0
        j = 0
        
        
        if len(s) > len(t):
            return False
        
        if (len(s) < 1 or len(t) < 1) :
            return True

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
                if i == len(s):
                    return True
            else:
                j += 1
                
        return False
