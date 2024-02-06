class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        l = len(s)-1  
        ogl = len(s)-1  

        # if l == 1:
        while l >= 0:
            if s[l] == ' ':
                return ogl - l
            l -=1 
        return len(s)
    
