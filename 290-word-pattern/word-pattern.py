class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        valdict = {}
        s = (s.split(' '))
        if len(set(s)) !=  len(set(pattern)):
            return False
        if len(s) != len(pattern):
            return False

        for i in range(len(pattern)):
            if s[i] not in valdict:
                valdict[s[i]] = pattern[i]
           
            elif valdict[s[i]] != pattern[i]:
                return False

        return True
            
