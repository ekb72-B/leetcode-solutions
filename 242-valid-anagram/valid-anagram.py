class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dics = {}
        dicc = {}
        for i in s:
            if i not in dics:
                dics[i] = 0
            else:
                dics[i] += 1
        
        for i in t: 
            if i not in dicc:
                dicc[i] = 0
            else:
                dicc[i] += 1
        
        return dicc == dics