class Solution:
    def firstUniqChar(self, s: str) -> int:
        chardict = {}
        res = -1

        for char in s:
            if char not in chardict:
                chardict[char] = 1
            else:
                chardict[char] += 1
        
        for key, value in chardict.items():
            if value == 1:
                return s.index(key)
        
        return -1

            