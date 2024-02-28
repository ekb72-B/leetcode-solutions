class Solution:
    def firstUniqChar(self, s: str) -> int:
        chardict = {}
        res = []
        nres = []
        idx = 0

        for char in s:
            if char not in chardict:
                chardict[char] = idx
            else:
                chardict[char] = -1
            idx += 1
        
        for value in chardict.values():
            if value != -1:
                return value
        return -1
        
     

            