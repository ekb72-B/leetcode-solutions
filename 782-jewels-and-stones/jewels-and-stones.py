class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jdict = {}
        ctr = 0
        for j in jewels:
            if j not in jdict:
                jdict[j] = 1
            else:
                continue
    
        for s in stones:
            if s in jdict:
                ctr += 1
        
        return ctr

    