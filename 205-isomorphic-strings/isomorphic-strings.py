class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        smap = []
        tmap = []

        for i in s:
            smap.append(s.index(i))
        for i in t:
            tmap.append(t.index(i))

        return smap == tmap
