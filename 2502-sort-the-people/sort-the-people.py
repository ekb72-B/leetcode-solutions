class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        nhdict = {}
        res = []

        for i in range(len(names)):
            nhdict[heights[i]] = names[i]

        hs = sorted(heights)[::-1]
        
        for i in hs:
            res.append(nhdict[i])
        return res
