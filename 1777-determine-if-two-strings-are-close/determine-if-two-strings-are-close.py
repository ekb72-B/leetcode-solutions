class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # if their lengths are the same and their sets are the same 
        if len(word1) != len(word2):
            return False
        
        print (Counter(word1))
        if set(word1) == set(word2) and sorted(list(self.dictify(word1).values())) == sorted(list(self.dictify(word2).values())):
            return True
            
        return False

    def dictcheck(self, dict1,dict2):
        for i in dict1:
            if i not in dict2:
                return False
            else:
                return dict1[i] == dict2[i]

    
    def dictify(self, word):
        wdict = {}
        for char in word:
            if char in wdict:
                wdict[char] += 1
            else:
                wdict[char] = 1
        return wdict 