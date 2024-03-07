class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # l1 = "qwertyuiop"
        # l2 = "asdfghjkl"
        # l3 = "zxcvbnm"
        res = []

        l1 = {'q','w','e','r','t','y','u','i','o','p'}
        l2 = {'a','s','d','f','g','h','j','k','l'}
        l3 = {'z','x','c','v','b','n','m'}

        for word in words:
            worda = set(word.lower())
            if (worda&l1 == worda) or(worda&l2 == worda) or (worda&l3 == worda):
                #This shows set intersections
                res.append(word)
        return res