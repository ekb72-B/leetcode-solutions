class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        l1 = "qwertyuiop"
        l2 = "asdfghjkl"
        l3 = "zxcvbnm"
        res = []

        for word in words:
            worda = word.lower()

            if len(set(l1+worda)) == len(l1) or len(set(l2+worda)) == len(l2) or len(set(l3+worda))== len(l3): 
                res.append(word)
        return res