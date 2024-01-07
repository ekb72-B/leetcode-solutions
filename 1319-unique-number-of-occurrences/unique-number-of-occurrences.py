class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arrdict = {}
        for i in arr:
            if i in arrdict:
                arrdict[i] += 1
            else:
                arrdict[i] = 1

        for key,values in enumerate(arrdict):
            if len(set(arrdict.values())) < len(arrdict):
                return False
        return True 