class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return [s.index(c) for c in s] == [t.index(c) for c in t]
        # if len(s) != len(t):
        #     return False

        # if len(set(s)) != len(set(t)):
        #     return False

        # p1 = 0
        # p2 = 0
        # vdict = {}
        # tdict = {}
        # for i in range(len(s)):  
        #     if s[i] not in vdict:
        #         vdict[s[i]] = t[i]
        #     if t[i] not in tdict:
        #         tdict[t[i]] = s[i]
        #     else:
        #         if vdict[s[i]] != t[i] or tdict[t[i]] != s[i]:
        #             return False     
        # return True