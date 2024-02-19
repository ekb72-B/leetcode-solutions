class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sdict = {}

        for i in range(len(s)):
            if s[i] not in sdict:
                sdict[s[i]] = t[i]
        
            keys = [k for k, v in sdict.items()]
            vals = [v for k, v in sdict.items()]

            if t[i] != sdict[s[i]] or len(set(keys)) != len(set(vals)) :
                return False
        return True
